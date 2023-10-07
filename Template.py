import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s] :(message)s:')
project_name = 'textsummarizer' #it is source that will have all component
list_of_files=[
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "app.py",
    "params.yaml",
    "Dockerfile",
    "requirement.txt",
    "research/trails.ipynb",
    "setup.py",
    "main.py",
    "test.py"
]

for file in list_of_files:
    file= Path(file)
    file_dir, file_name = os.path.split(file)

    if file_dir!='':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory {file_dir} for {file_name}")

    if (not os.path.exists(file)) or (os.path.getsize(file)):
        with open(file,'w') as f:
            pass
        logging.info(f"creating empty file : {file}")

    else:
        logging.info(f"{file_name} already existpy")