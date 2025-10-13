import subprocess

def run_in_docker(docker_image: str, host_submission_path: str, lang_key: str, runner_file: str):
    """
    Runs the submission in a Docker container and returns the output.
    Returns a tuple: (final_output, passed_count, total_tests, is_compile_error)
    """
    container_work_dir = "/app"
    command_to_run = ""

    if lang_key == "java":
        runner_class_name = runner_file.replace(".java", "")
        command_to_run = f"javac *.java && java {runner_class_name}"
    elif lang_key == "python":
        command_to_run = f"python3 {runner_file}"

    docker_command = [
        "docker", "run", "--rm", "--network", "none",
        "-v", f"{host_submission_path}:{container_work_dir}",
        "--workdir", container_work_dir, docker_image,
        "sh", "-c", command_to_run
    ]

    run_process = subprocess.run(docker_command, capture_output=True, text=True, timeout=60) # Increased timeout

    final_output = run_process.stdout + run_process.stderr
    passed_count, total_tests = 0, 0
    is_compile_error = (lang_key == "java" and "error:" in run_process.stderr and "[SUMMARY]:" not in run_process.stdout)

    for line in run_process.stdout.splitlines():
        if line.startswith("[SUMMARY]:"):
            try:
                parts = line.strip().split(':')
                passed_count, total_tests = int(parts[1]), int(parts[2])
            except (ValueError, IndexError):
                pass

    return (final_output, passed_count, total_tests, is_compile_error)