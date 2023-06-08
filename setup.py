from setuptools import find_packages, setup

def get_requirements(file_path):
    '''
    this function returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

setup(
name = 'miproject',
version = '0.0.1',
author = 'Sagar',
author_email = 'spadhiyar230595@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

