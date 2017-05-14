from setuptools import setup
from sys import platform

data_files=[]

if platform == "linux" or platform == "linux2":
    data_files=[("/etc/bash_completion.d/", ["bin/ignr_complete"])]
elif platform == "darwin":
    data_files=[("/usr/local/etc/bash_completion.d/", ["bin/ignr_complete"])]


setup(
    name='ignr',
    description='Python command line client to download' \
                '.gitignore templates from gitignore.io',
    version='1.1',
    url='https://github.com/Antrikshy/ignr',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    scripts=['bin/ignr'],
    packages=['ignr'],
    license='MIT',
    keywords='git gitignore gitignore.io developer',
    data_files=data_files
)