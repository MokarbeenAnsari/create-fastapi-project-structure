import os
import sys

def create_project_structure(base_path):
    # Define the names of directories to be created
    paths = [
        os.path.join(base_path, "app"),
        os.path.join(base_path, "app", "models"),
        os.path.join(base_path, "app", "routers"),
        os.path.join(base_path, "app", "schemas"),
        os.path.join(base_path, "app", "tests"),
        os.path.join(base_path, "app", "database"),
    ]

    for path in paths:
        try:
            os.makedirs(path)
            # Create an __init__.py in each directory except for the 'app' directory
            if path != os.path.join(base_path, "app"):
                open(os.path.join(path, "__init__.py"), 'a').close()
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")

    # Create files
    files = [
        os.path.join(base_path, "app", "main.py"),
        os.path.join(base_path, "Dockerfile"),
        os.path.join(base_path, "docker-compose.yml"),
        os.path.join(base_path, "requirements.txt"),
    ]

    for file in files:
        try:
            open(file, 'a').close()
        except OSError:
            print(f"Creation of the file {file} failed")
        else:
            print(f"Successfully created the file {file}")

if len(sys.argv) != 2:
    print("Usage: python script_name.py <project_name>")
else:
    create_project_structure("./" + sys.argv[1])
