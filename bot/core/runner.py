import subprocess
import os

def run_in_docker(docker_image: str, host_submission_path: str, lang_data: dict):
    """
    Runs the submission in a Docker container and returns the output.
    Returns a tuple: (final_output, passed_count, total_tests, is_compile_error)
    """
    container_work_dir = "/app"

    runner_file = os.path.basename(lang_data["test_runner"])
    runner_class_name = runner_file.split('.')[0]

    compile_cmd_template = lang_data.get("compile_command") # This can be None
    run_cmd_template = lang_data["run_command"]

    placeholders = {
        "runner_file": runner_file,
        "runner_class_name": runner_class_name
    }

    formatted_run_cmd = run_cmd_template.format(**placeholders)

    command_to_run_in_container = ""

    if compile_cmd_template:
        formatted_compile_cmd = compile_cmd_template.format(**placeholders)
        command_to_run_in_container = f"{formatted_compile_cmd} && {formatted_run_cmd}"
    else:
        command_to_run_in_container = formatted_run_cmd

    docker_command = [
        "docker", "run", "--rm", "--network", "none",
        "-v", f"{host_submission_path}:{container_work_dir}",
        "--workdir", container_work_dir, docker_image,
        "sh", "-c", command_to_run_in_container
    ]

    run_process = subprocess.run(docker_command, capture_output=True, text=True, timeout=60)

    final_output = run_process.stdout + run_process.stderr
    passed_count, total_tests = 0, 0
    is_compile_error = (bool(compile_cmd_template) and "error:" in run_process.stderr and "[SUMMARY]:" not in run_process.stdout)

    for line in run_process.stdout.splitlines():
        if line.startswith("[SUMMARY]:"):
            try:
                parts = line.strip().split(':')
                passed_count, total_tests = int(parts[1]), int(parts[2])
            except (ValueError, IndexError):
                pass

    return (final_output, passed_count, total_tests, is_compile_error)