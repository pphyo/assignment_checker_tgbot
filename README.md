# Assignment Checker Telegram Bot

This project is a Telegram bot designed to automatically check and grade programming assignments in multiple languages (Java, Python, etc.). It uses Docker to create secure, isolated environments for compiling and running student code against predefined test cases.

## Server Setup Guide

This guide provides the necessary steps to deploy and run the bot on a new Linux server (e.g., an AWS EC2 instance running Ubuntu).

### Prerequisites

1. A running Linux server (Ubuntu 22.04 LTS is recommended).
2. You have SSH access to the server.
3. Your bot project is hosted on a Git repository (e.g., GitHub).

---

### Step 1: Update Server and Install Dependencies

Log into your server via SSH. Update packages and install essential software: Python, Pip, Git, and Docker.

```bash
# Update package lists
sudo apt update && sudo apt upgrade -y

# Install Python, Pip, Git, and Docker
sudo apt install -y python3-pip git docker.io

# Start and enable the Docker service to run on boot
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 2: Grant Docker Permissions

To run Docker commands without `sudo`, add your current user to the `docker` group.

```bash
# Add your user to the docker group
sudo usermod -aG docker ${USER}

# IMPORTANT: You must log out and log back in for this change to take effect.
exit
```

After logging back in, verify by running `docker ps` without `sudo`.

### Step 3: Clone Your Project Repository

Clone your bot's source code from your Git repository.

```bash
# Replace the URL with your actual repository URL
git clone <repository-url>

# Navigate into the project directory
cd <repository-name>/
```

### Step 4: Install Python Libraries

Install the required Python libraries using the `requirements.txt` file.

```bash
pip3 install -r requirements.txt
```

### Step 5: Configure the Bot

The bot uses a `.env` file for secret credentials. This file is ignored by Git for security.

1. **Create a `.env` file:**

    ```bash
    nano .env
    ```

2. **Add your Bot Token to the file:**
    Add the following line, replacing the placeholder with your token from BotFather.

    ```bash
    BOT_TOKEN="YOUR_ACTUAL_BOT_TOKEN_HERE"
    ```

    Save and exit (`Ctrl+X`, `Y`, `Enter`).

### Step 6: Build Docker Images

Build the Docker images required for each programming language.

```bash
# Build the Java environment
docker build -f java.Dockerfile -t java-checker-env .

# Build the Python environment
docker build -f python.Dockerfile -t python-checker-env .
```

### Step 7(A): Run the Bot Persistently

Use a terminal multiplexer like `tmux` to keep the bot running after you disconnect.

1. **Start a new `tmux` session:**

    ```bash
    tmux new -s bot_session
    ```

2. **Run the bot inside the session:**

    ```bash
    python3 bot.py
    ```

3. **Detach from the session:**
    Press **`Ctrl+B`**, then press **`D`**. Your bot is now running in the background.

### Step 7(B): Run the Bot with auto start when OS boot up

1. copy the bot_autostart.service to /etc/systemd/system/
2. sudo systemctl daemon-reload
3. sudo systemctl enable bot_autostart.service
4. sudo systemctl start bot_autostart.service
5. If you edit the bot_autostart.service, then edit the file
6. And do the step 2, 3, 4

### Managing the Bot

* **To re-attach:** `tmux attach -t bot_session`
* **To stop the bot:** Re-attach and press `Ctrl+C`.

---

## Project Structure Overview

```bash
.
├── assignments/
│   ├── roman_to_integer/
│   │   ├── java/
│   │   │   ├── RomanToInteger.java      (Template)
│   │   │   └── RomanToIntegerTestRunner.java
│   │   ├── python/
│   │   │   ├── RomanToInteger.py        (Template)
│   │   │   └── roman_to_integer_runner.py
│   │   └── description.md
│   └── ... (other assignments)
├── users/                  (Ignored by Git)
├── .env                    (Ignored by Git)
├── .gitignore
├── assignments.json
├── bot.py
├── Dockerfile              (For Java)
├── python.Dockerfile       (For Python)
└── requirements.txt
```

## How to Add a New Assignment

1. Create a new directory in `assignments/` (e.g., `assignments/new_problem/`).
2. Inside, create a `description.md` file.
3. For each language you want to support (e.g., `java`, `python`):
    * Create a sub-directory (e.g., `assignments/new_problem/java/`).
    * Add the code template file (e.g., `NewProblem.java`).
    * Add the test runner file (e.g., `NewProblemTestRunner.java`).
4. Update `assignments.json` with the new assignment's configuration, including paths for all supported languages.
5. If a new language requires a new environment, create a new `Dockerfile` and build its image on the server.
6. Restart the bot on the server.
