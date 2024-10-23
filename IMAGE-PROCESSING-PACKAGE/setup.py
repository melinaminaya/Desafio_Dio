from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
    
setup(
    name='IMAGE-PROCESING-PACKAGE',
    version = '0.0.1',
    author='Melina',
    author_email="melina.minaya@gmail.com",
    description='My short description of',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='mygithub.com',
    packages=find_packages(),
    install_requires=requirements, #somente se houver dependência
    python_requires='>=3.8',
)