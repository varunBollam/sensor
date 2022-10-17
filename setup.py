# to create packages
from setuptools import find_packages,setup

def get_requirements():
    with open("requirements.txt") as f:
        requirements_list=[]
        for line in f:
            requirements_list.append(line.strip('\n'))
        return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Varun",
    author_email="dsvarunbollam@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)