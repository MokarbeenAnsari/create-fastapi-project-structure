# FastAPI Project Structure Creation Script

This repository provides a Python script for setting up a basic FastAPI project structure.

## Structure

The script creates the following directory and file structure:

```
<project_name>/
├── app/
│ ├── main.py
│ ├── models/
│ │ └── init.py
│ ├── routers/
│ │ └── init.py
│ ├── schemas/
│ │ └── init.py
│ ├── tests/
│ │ └── init.py
│ └── database/
│ └── init.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
### Explanation

- `<project_name>`: The root directory of the project, which is named according to the argument you pass to the script.
- `app`: The directory that contains the core application code.
    - `main.py`: The main application file. It is where you'll initialize and configure your FastAPI application.
    - `models`: A directory for SQLAlchemy models, which represent the structure of your database.
    - `routers`: A directory for route details. In FastAPI, you can modularize route handlers using routers.
    - `schemas`: A directory for Pydantic models, which serve as request and response schemas.
    - `tests`: A directory for test cases to ensure your application works as expected.
    - `database`: A directory for database related operations such as connections, configurations, etc.
- `Dockerfile`: The Dockerfile for building a Docker image for the application.
- `docker-compose.yml`: The Docker Compose file that can be used to define and run multi-container Docker applications.
- `requirements.txt`: A file listing the Python dependencies of the project, which can be installed using pip.

## How to Use

1. Clone this repository.

2. Open a terminal/command prompt.

3. Navigate to the directory containing the script.

4. Run the script, providing the name of your project as an argument:
```
    python create.py your_project_name
```

Replace `your_project_name` with the name you want for your FastAPI project. This will be used as the name of the root directory for your new project.


