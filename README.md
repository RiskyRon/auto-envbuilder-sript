# auto-envbuilder-sript

# GPT-BuildBox Python Project Builder

## Introduction
This script automates the process of setting up a new Python project with a dedicated virtual environment, a SQLite database, and a Docker environment. The script offers several configurable options:
- `--dir`: The directory name for the new project. Default is 'project'.
- `--venv`: The name of the Python virtual environment to create. Default is 'venv'.
- `--packages`: A comma-separated list of Python packages to install in the virtual environment. Default is an empty list.
- `--python`: The version of Python to use in the virtual environment. Default is '3.11.3'.

## Example Usage
To create a new project with the directory name 'my_cool_project', a virtual environment named 'my_env', and the packages 'numpy', 'pandas', and 'matplotlib' installed, using Python version 3.11.3, you would run the following command:
```python3 main.py --dir my_cool_project --venv my_env --packages numpy,pandas,matplotlib --python 3.11.3```

## Docker Commands
Here are some Docker commands you might find useful:
### Build Docker Image
```docker-compose build```
### Start Docker Containers
```docker-compose up -d```
### Stop Docker Containers
```docker-compose down```
### List Docker Containers
```docker ps -a```
### Execute a Command Inside a Docker Container
```docker exec -it <container-id> <command>```
Replace `<container-id>` with the ID of your Docker container, and `<command>` with the command you want to execute.
For example, to run a Python script named 'openai_script.py' located in the '/app' directory inside the Docker container, you would use the following command:
```docker exec -it <container-id> python /app/openai_script.py```

## Project Structure
The script creates the following project structure:
```
project/
│   ├── app/
│   ├── config/
│   │   ├── .env
│   │   ├── .gitignore
│   │   ├── .vscode/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── RONTESTING/
│   │   ├── database.sqlite3
│   │   ├── docker-compose.yml
│   │   ├── openai_script.py
│   │   ├── requirements.txt
│   │   ├── tests/
│   │   └── venv/
│   └── WORKSPACE/
```

## Activating the Virtual Environment
After running the script, you can activate the virtual environment and start the Docker containers using the following command:
```source <project-dir>/<venv>/bin/activate && cd <project-dir>/config/ && docker-compose up -d```
Replace `<project-dir>` with the name of your project directory, and `<venv>` with the name of your virtual environment.
