from setuptools import setup, find_packages
from typing import List





##declaring variable for setup function
PROJECT_NAME="Housing-Predictor"
VERSION= "0.0.1"
AUHTOR= " Shubham musmade"
DESCRIPTION=" THIS IS MY FIRST MACHINE LEARNING PROJECT"

REQUIREMENT_FILE_NAME="requirements.txt"



def get_requirements_list()->List[str]:
    """
    description: this function is going to return list of
    requiurement ,emtion in requirements.txt file

    retun this function is going to return a list wi=hich contain 
    name of libraries in requirements.txt file
    """


    with open (REQUIREMENT_FILE_NAME) AS requirement_file:
        return requirement_file.readlines().remove("-e .")


## -e . will install housing package directly

setup(
name=PROJECT_NAME,
version= VERSION,
auhtor=AUHTOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()


)








