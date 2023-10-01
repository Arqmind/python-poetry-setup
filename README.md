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

# Pylint

Pylint is a widely used static code analysis tool for Python that helps identify errors, enforce coding standards, and promote code consistency. Here's a step-by-step guide on how to use Pylint:

### Install Pylint:

If you don't have Pylint installed, you can install it using pip, Python's package installer:

```css
pip install pylint
```

### Running Pylint on a Python file:

To run Pylint on a specific Python file, use the following command:

```
pylint your_file.py
```

Replace `your_file.py` with the name of the Python file you want to analyze.

### Customizing Pylint Configuration:

Pylint allows you to customize its behavior using a configuration file. Create a `pylint.rc` file in your project directory or use an existing one. Here's an example of a basic configuration file:

```ini
Copy code
[FORMAT]
max-line-length = 120

[MESSAGES CONTROL]
disable = C0301
```

In this example, we set the maximum line length to 120 characters and disable the C0301 message (line too long) to ignore that particular message.

### Running Pylint with a Configuration File:

To use a custom configuration file, specify it when running Pylint:

```css
Copy code
pylint --rcfile=pylint.rc your_file.py
```

### Output and Messages:

Pylint provides detailed output with messages and suggestions for improvement. It also assigns a score to your code based on the analysis. Higher scores indicate better code quality.

### Integrating with IDEs or Editors:

Pylint can be integrated into popular code editors or IDEs, such as VS Code, PyCharm, Sublime Text, etc. Check the specific documentation for your chosen editor to set up Pylint integration.

### Using Pylint with Continuous Integration (CI):

You can integrate Pylint into your continuous integration process to enforce code quality checks automatically. For example, you can run Pylint as a step in your CI/CD pipeline and fail the build if Pylint reports errors or warnings.

### Further Customization and Advanced Usage:

Pylint provides various command-line options for further customization, such as specifying the error types to display, setting output formats, etc. Refer to the Pylint documentation for more details on available options and advanced usage.

By using Pylint regularly and addressing the reported issues, you can improve the quality and maintainability of your Python code.

# Black

"Black" is a popular Python code formatting tool that automatically formats Python code to comply with a consistent style.

To set up Black for formatting Python code, follow these steps:

### Install Black:

Start by installing Black using pip, which is the package installer for Python.

```

pip install black

```

### Usage:

After installing Black, you can use it to format your Python code.

```

black <file_or_directory>

```

Black will recursively scan the directory for Python files and format them.

### Integration with Editors:

#### Visual Studio Code (VSCode):

Install the "Python" extension by Microsoft, which includes support for formatting with Black. Open your Python file, right-click, and choose "Format Document" or use the default keyboard shortcut (Shift + Alt + F on Windows/Linux or Shift + Option + F on Mac).

#### PyCharm:

Black can be integrated into PyCharm as an external tool. Go to "File" > "Settings" > "Tools" > "External Tools." Click the "+" icon to add a new tool and configure it to run Black with the desired arguments.

#### Other Editors:

Configure Black to run as a pre-commit hook or integrate it with other editors according to their respective plugins or extensions.

### Configuration:

Black follows a strict formatting style, but you can customize some aspects of its behavior using a configuration file or command-line options. Create a pyproject.toml file in your project directory with the following content:

```toml
#toml
[tool.black]
line-length = 79
target-version = ['py38']
include = '\.pyi?$'
exclude = ''
```

Adjust the settings as per your requirements.

# isort

isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. It provides a command line utility, Python library and plugins for various editors to quickly sort all your imports. It requires Python 3.7+ to run but supports formatting Python 2 code too.

Fore more details see [here](https://pycqa.github.io/isort/)

# pre-commit

Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

### Installation

Using poetry:

```
poetry add pre-commit
```

Using pip:

```
pip install pre-commit
```

Using homebrew:

```
brew install pre-commit
```

#### Check version

```
pre-commit --version
pre-commit 3.4.0
```

### Add a pre-commit configuration

create a file named .pre-commit-config.yaml
you can generate a very basic configuration using pre-commit sample-config
the full set of options for the configuration are listed [here](https://pre-commit.com/#plugins)
this example uses a formatter for python code, however pre-commit works for any programming language
See [here](https://pre-commit.com/hooks.html) for other supported hooks

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
```

or see the [.pre-commit-config.yaml](.pre-commit-config.yaml)

### Install the git hook script

```
pre-commit install
```

Now pre-commit will run automatically on git commit!

#### [Optional] Run it manually

```css
$ pre-commit run --all-files
[WARNING] Unexpected key(s) present at root: ignore
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/PyCQA/pylint.
[INFO] Initializing environment for https://github.com/PyCQA/pylint:pylint.
[INFO] Initializing environment for https://github.com/pre-commit/mirrors-mypy.
[INFO] Initializing environment for https://github.com/pre-commit/mirrors-mypy:requests.
[INFO] Initializing environment for https://github.com/PyCQA/isort.
[INFO] Initializing environment for https://github.com/PyCQA/isort:isort.
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Initializing environment for https://github.com/psf/black:black.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/PyCQA/pylint.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/pre-commit/mirrors-mypy.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/PyCQA/isort.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing pyproject.toml

Check Yaml...............................................................Passed
Check for added large files..............................................Passed
pylint...................................................................Passed
mypy.....................................................................Passed
isort....................................................................Passed
black....................................................................Passed

```
