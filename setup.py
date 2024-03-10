from setuptools import find_packages,setup
from typing import List

def get_requirement(file:str)->List[str]:
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name = 'ML Project 1',
    version = '0.0.1',
    author = 'Anvai Shrivastava',
    author_email = 'anvaishrivastava@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement('requirements.txt')
)