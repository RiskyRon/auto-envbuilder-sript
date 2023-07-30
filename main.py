
"""
This script creates a new Python project with the following configurable options:

--dir       : The directory name for the new project. Default is 'my_project'.
--venv      : The name of the Python virtual environment to create. Default is 'venv'.
--packages  : A comma-separated list of Python packages to install in the virtual environment. Default is an empty list.
--python    : The version of Python to use in the virtual environment. Default is '3.11.3'.

Example usage:
python build_script.py --dir my_cool_project --venv my_env --packages numpy,pandas,matplotlib --python 3.11.3
"""



import subprocess
import argparse
import sqlite3
import logging
import json
import os


def create_directory(dir_name):
    logging.info(f"Creating directory {dir_name}")
    if os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} already exists.")
        return False

    try:
        os.makedirs(dir_name, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory {dir_name}: {e}")
        return False

    return True

def create_ron_testing_dir():
    logging.info("Creating RONTESTING directory")
    os.makedirs("RONTESTING", exist_ok=True)

def setup_pytest():
    os.makedirs("tests", exist_ok=True)
    with open("tests/test_initial.py", "w") as f:
        f.write("""def test_initial():\n    assert True""")


def create_sqlite_db(db_name):
    conn = sqlite3.connect(db_name)
    logging.info(f"Created SQLite database {db_name}")
    conn.close()

def create_virtual_env(venv_name, python_version):
    logging.info(f"Creating virtual environment {venv_name} with Python version {python_version}")
    subprocess.call(["virtualenv", "-p", f"python{python_version}", venv_name])
    return venv_name

def install_packages(venv_name, packages):
    for package in packages:
        subprocess.call([f"{venv_name}/bin/pip", 'install', package])

def create_vscode_settings(venv_name):
    settings = {
        "python.pythonPath": f"{venv_name}/bin/python"
    }
    os.makedirs(".vscode", exist_ok=True)
    with open(".vscode/settings.json", "w") as f:
        json.dump(settings, f, indent=4)

def create_docker_files():
    with open("Dockerfile", "w") as f:
        f.write("FROM python:3.8\n")
        f.write("WORKDIR /app\n")
        f.write("COPY requirements.txt .\n")
        f.write("RUN pip install -r requirements.txt\n")
        f.write("COPY . .\n")
        f.write('CMD ["python", "your_script.py"]')

    with open(".dockerignore", "w") as f:
        f.write(".git\n")
        f.write(".vscode\n")
        f.write("*.pyc\n")
        f.write("*.pyo\n")
        f.write("*.pyd\n")
        f.write("__pycache__\n")
        f.write(".Python\n")
        f.write("env\n")
        f.write("pip-log.txt\n")
        f.write("pip-delete-this-directory.txt\n")

def create_env_file():
    default_env_vars = [
        "#openai",
        "OPENAI_API_KEY=",
        "#aws",
        "S3_BUCKET=",
        "AWS_ACCESS_KEY_ID=",
        "AWS_SECRET_ACCESS_KEY=",
        "AWS_REGION=",
        "#django",
        "DJANGO_SECRET_KEY=",
        "#pinecone",
        "DATASTORE=pinecone",
        "PINECONE_API_KEY=",
        "PINECONE_ENVIRONMENT=",
        "PINECONE_INDEX="
    ]
    with open('.env', 'w') as f:
        f.write('\n'.join(default_env_vars))

def create_readme(python_version,dir_name):
    with open("README.md", "w") as f:
        f.write(f"# {dir_name}\n")
        f.write(f"This project uses Python version {python_version}.\n")
        f.write("Further project details will be added here.")


def create_gitignore_file(venv_name):
    default_ignore_files = [
        venv_name,  
        "database.sqlite3",
        "RONTESTING/", 
        ".env", 
        "__pycache__/",  # Ignore Python cache files
        "*.pyc",  # Ignore Python compiled files
        "*.pyo",
        "*.pyd",
        ".Python",
        "ipynb_checkpoints/",  # Ignore Jupyter Notebook checkpoints
        ".vscode/",  # Ignore VS Code settings
        ".idea/",  # Ignore PyCharm settings
        "*.log",  # Ignore all log files
        ".DS_Store",  # Ignore Mac system files
        "dist/",  # Ignore Python distribution folder
        "build/",  # Ignore Python build folder
        "*.egg-info/",  # Ignore Python egg info
        ".pytest_cache/",  # Ignore pytest cache
        ".mypy_cache/",  # Ignore mypy type checker cache
    ]
    with open('.gitignore', 'w') as f:
        f.write('\n'.join(default_ignore_files))

def initialize_git_repo():
    logging.info("Initializing Git repository")
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'checkout', '-b', 'main'])  # switch to a new branch 'main'
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])

def print_activate_virtual_env_command(venv_name,dir_name):
    print("\n\n" + "#" * 30)
    print(f"To activate the virtual environment, run:")
    print(f"source {dir_name}/{venv_name}/bin/activate")
    print("#" * 30 + "\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Python project")
    parser.add_argument("--dir", help="Directory name", default="my_project")
    parser.add_argument("--venv", help="Virtual environment name", default="venv")
    parser.add_argument("--packages", help="Packages to install (separated by commas)", default="")
    parser.add_argument("--python", help="Python version", default="3.11.3")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    if not create_directory(args.dir):
        logging.error("Failed to create directory")
        exit(1)

    os.chdir(args.dir)
    venv_name = create_virtual_env(args.venv, args.python)
    create_sqlite_db('database.sqlite3')
    create_ron_testing_dir()
    create_readme(args.python,args.dir)
    create_env_file()
    create_gitignore_file(venv_name)
    packages = args.packages.split(',') if args.packages else []
    install_packages(venv_name, packages)
    create_vscode_settings(venv_name)
    setup_pytest()
    create_docker_files()
    initialize_git_repo()
    print_activate_virtual_env_command(venv_name,args.dir)
