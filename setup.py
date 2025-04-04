''' The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptool (or disutils in older versions of python) to define the configurations 
of your project such as meta data , dependencies and many more...'''

from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from files
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name = "Network Security",
    version="0.0.1",
    author="Jahid Hasan",
    author_email="jmhasan17@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
