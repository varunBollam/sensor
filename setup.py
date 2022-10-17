# to create packages
from setuptools import find_packages,setup
'''
def get_requirements():
    with open("requirements.txt") as f:
        requirements_list:List[str]=[]
        for line in f:
            requirements_list.append(line.strip('\n'))
        return requirements_list
'''
def get_requirements():
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open("requirements.txt") as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if "-e ." in requirement_list:
            requirement_list.remove('-e .')
        return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Varun",
    author_email="dsvarunbollam@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)