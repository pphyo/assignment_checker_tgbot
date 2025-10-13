# Telegram Java Assignment Checker Bot

This project is a Telegram bot designed to automatically check and grade Java programming assignments submitted by students. It uses Docker to create a secure and isolated environment for compiling and running student code against predefined test cases.

## Server Setup Guide

This guide provides the necessary steps to deploy and run the bot on a new Linux server (e.g., an AWS EC2 instance running Ubuntu).

### Prerequisites

1. A running Linux server (Ubuntu 22.04 LTS is recommended).
2. You have SSH access to the server.
3. Your bot project is hosted on a Git repository (e.g., GitHub).

---

### Step 1: Update Server and Install Dependencies

First, log into your server via SSH. Then, update the package lists and install essential software: Python, Pip (Python's package manager), Git, and Docker.

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

By default, Docker requires `sudo` for every command. To run Docker commands without `sudo`, add your current user to the `docker` group.

```bash
# Add your user to the docker group
sudo usermod -aG docker ${USER}

# IMPORTANT: You must log out and log back in for this change to take effect.
exit
```

After running the commands above, close your SSH session and log back in. You should now be able to run `docker ps` without `sudo`.

### Step 3: Clone Your Project Repository

Clone your bot's source code from your Git repository to the server.

```bash
# Replace the URL with your actual repository URL
git clone [https://github.com/pphyo/assignment_checker_tgbot.git](https://github.com/pphyo/assignment_checker_tgbot.git)

# Navigate into the project directory
cd assignment_checker_tgbot/
```

### Step 4: Install Python Libraries

Install the required Python library (`python-telegram-bot`) using `pip`. It is best practice to use a `requirements.txt` file.

First, create a `requirements.txt` file in your project directory:

```bash
# requirements.txt
python-telegram-bot
python-dotenv
```

Then, install the libraries from this file:

```bash
pip3 install -r requirements.txt
```

### Step 5: Configure the Bot

Before running the bot, you need to set your Telegram Bot Token.

1. **Edit the `bot.py` file:**
    Open the `bot.py` file using a text editor like `nano` or `vim`.

    ```bash
    nano bot.py
    ```

2. **Update the Bot Token:**
    Find the line `BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"` and replace the placeholder with your actual token from BotFather. Save and exit the editor (`Ctrl+X`, then `Y`, then `Enter` for nano).

3. **Verify `assignments.json`:**
    Ensure your `assignments.json` file is up-to-date with all the assignments you want to launch.

### Step 6: Build the Docker Image

Build the Docker image that will be used to run the student's code. This command only needs to be run once.

```bash
# Make sure you are in the root directory of your project (where the Dockerfile is)
docker build -t assignment-checker-env .
```

### Step 7: Run the Bot Persistently

To ensure your bot keeps running even after you close your SSH session, you should use a terminal multiplexer like `tmux`.

1. **Install `tmux` (if not already installed):**

    ```bash
    sudo apt install -y tmux
    ```

2. **Start a new `tmux` session:**
    Give your session a meaningful name, like `bot`.

    ```bash
    tmux new -s ac_bot
    ```

3. **Run the bot inside the `tmux` session:**
    Now, you are inside a new terminal session. Start the bot as usual.

    ```bash
    python3 bot.py
    ```

    You will see the "Bot starting..." messages. The bot is now running.

4. **Detach from the `tmux` session:**
    You can now safely detach from this session, and it will keep running in the background. Press the following key combination:
    **`Ctrl+B`** (release the keys), then press **`D`**.

You can now close your SSH connection. Your bot will remain online.

### Managing the Bot with `tmux`

* **To re-attach to the session** (to view logs or stop the bot):

    ```bash
    tmux attach -t ac_bot
    ```

* **To stop the bot**, re-attach to the session and press `Ctrl+C`.

---

## Project Structure Overview

```bash
.
├── assignments/
│   ├── integer_to_roman/
│   │   ├── description.md
│   │   └── IntegerToRomanTestRunner.java
│   └── ... (other assignments)
├── users/
│   └── ... (user data will be created here)
├── assignments.json
├── .evn
├── bot.py
├── Dockerfile
└── requirements.txt
```

## How to Add a New Assignment

1. Create a new sub-directory inside the `assignments/` folder (e.g., `assignments/new_assignment/`).
2. Add your `TestRunner.java` file and `description.md` file into the new directory.
3. Update the `assignments.json` file with a new entry for `new_assignment`.
4. Restart the bot on the server (re-attach to the `tmux` session, stop with `Ctrl+C`, and run `python3 bot.py` again).
