# to create packages
from setuptools import find_packages,setup

"""def get_requirements()->List[str]:
     this function gives you list of requirements

    requirements_list:List[str]=[]
    
    
    write code to read requirement.txt
    
    return requirements_list
    """
setup(
    name="sensor",
    version="0.0.1",
    author="Varun",
    author_email="dsvarunbollam@gmail.com",
    packages=find_packages(),
    install_requires=[],
)