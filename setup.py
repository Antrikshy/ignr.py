from setuptools import setup

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
    keywords='git gitignore gitignore.io developer'
)