import os
from setuptools import setup

cwd = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(cwd) as f:
    dependencies = list(map(lambda x: x.replace("\n", ""), f.readlines()))

setup(
    name='thesis',
    version='0.1',
    install_requires=dependencies,
    packages=['gymrecsys'],
)