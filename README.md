# Poetry

Python packaging and dependency management made easy.

Using poetry for Python package management involves creating and managing a `pyproject.toml` file to define your project's dependencies and other configuration settings. Poetry is a modern Python dependency management tool that simplifies package installation and project management.

Here's a step-by-step guide to using Poetry for Python package management:

### Install Poetry:

You can use pip to install it globally:

```
pip install poetry
```

Create a new project or navigate to an existing one:
Create a new project directory or navigate to an existing Python project.

### Initialize a Poetry project:

Run the following command in the project directory to initialize a new Poetry project:

```
poetry init
```

Follow the setup prompts:
Poetry will prompt you to enter information about your project, including the project name, description, author, and license.

### Add dependencies:

After initialization, you can add project dependencies using the add command:

```
poetry add package-name
```

### Define versions and constraints:

Poetry allows you to specify package versions and constraints. For example:

```
peotry add package-name@^1.0
```

### Install Dependencies

```
poetry install
```

### Activate virtual env

```
poetry shell
```

### Update dependencies

```
poetry update
```

### dectivate virtual env

```
poetry deactivate
```

or type `exit`

### Locking the dependencies:

Poetry will generate a poetry.lock file that contains the exact versions of your dependencies. This ensures consistent installations across different environments.

### Exporting to requirements.txt

```
poetry export --format requirements.txt --output requirements.txt
```
