from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str):
    """
    _summary_:This function will return the list of requirements

    Args:
        file_path (str): Location of requirements.txt file.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    return requirements

setup(
    name='IncomeMlproject',
    version = '0.0.1',
    author='Gaurav',
    author_email='gauravy1905@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
