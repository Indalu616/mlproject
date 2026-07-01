# it is used to make my application a package
#  so that any other person can use it in their project
from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'
FILE_PATH = 'requirements.txt'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(name = 'mlproject',
      version = '0.0.1',
      author = 'Indalu',
      author_email ='endalukalbesa511@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements(FILE_PATH)
      )