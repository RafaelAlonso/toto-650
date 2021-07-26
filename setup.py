from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]


setup(name='toto',
      version='0.1.0',
      description="our own mega super blaster package",
      packages=find_packages(),
      install_requires=requirements,
      scripts=['scripts/sayhello'])