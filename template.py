import os
from pathlib import Path
import logging


#print(Path("a\\b\\c.txt"))


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformatio.py",
    "src/compenents/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logger.py",
    "src/exception/exception.py",
    "tests/units/__init__.py",
    "tests/integration/__init__.py",
    "init/setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.py.ipynb"
       
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # create an empty file
