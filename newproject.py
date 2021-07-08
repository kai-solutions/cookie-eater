import os
import shutil
from subprocess import call

SUBFOLDERS = {
    "data": ["raw", "processed", "interim", "external"],
    "reports": ["figures"],
}

OTHER_SUBFOLDERS = ["notebooks", "sql",
                    "src", "tests", "models", "logs", "docs"]


def set_directory():
    """
    set directories
    """

    current_directory = os.getcwd()
    project_name = input("NAME YOUR PROJECT: ")
    project_path = os.path.join(current_directory, project_name)

    return project_path


def main():
    project_path = set_directory()
    try:
        os.makedirs(project_path)
        x = True
    except:
        x = input(
            "Folder already exists. Type True to overwrite. Any other input to exit: "
        )
        if x.lower() != "true":
            x = False
        else:
            shutil.rmtree(project_path)
            print(f" Removing {project_path}")
    finally:
        if x:
            # creates respective folders in tree
            for folder in OTHER_SUBFOLDERS:
                os.makedirs(os.path.join(project_path, folder))
            for key, value in SUBFOLDERS.items():
                for v in value:
                    new_folder = os.path.join(key, v)
                    os.makedirs(os.path.join(project_path, new_folder))
        else:
            print("Project folder not created")

    open(os.path.join(project_path, ".gitignore"), "w+")
    open(os.path.join(project_path, ".requirements.txt"), "w+")
    open(os.path.join(project_path, ".README.md"), "w+")
    open(os.path.join(project_path, ".environment.yml"), "w+")
    open(os.path.join(project_path, ".setup.py"), "w+")

    for root, dirs, files in os.walk(project_path):
        if len(dirs) > 1:
            for d in dirs:
                if "src" not in d and "data" not in d and "reports" not in d:
                    open(os.path.join(root, d, ".gitkeep"), "w+")
                elif "src" in d:
                    open(os.path.join(root, d, "__init__.py"), "w+")

    def command(args=[], timeout=None, shell=True):
        ''' Executes shell commands by using subprocess module
        '''
        # combines separate arguments in one string
        command_str = ' '.join(args)
        print(command_str)
        # executes command
        call(command_str, timeout=timeout, shell=shell)

    virtual_env = input(
        "You may create a virtual python environment inside the folder directory as a best practice for DataScience shemas. Do you wish to create a python virtual environment inside the project folder? [Y] Yes [N] No (predetermined value is 'N'): ")
    if virtual_env == 'Y':
        # creates folder called venv inside project directory
        command(['python', '-m', 'venv', os.path.join(project_path, 'venv')])


if __name__ == "__main__":
    main()
