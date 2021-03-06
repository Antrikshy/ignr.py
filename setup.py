from setuptools import setup

setup(
    name='ignr',
    description='Python command line client to download' \
                '.gitignore templates from gitignore.io',
    version='2.0',
    url='https://github.com/Antrikshy/ignr',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    entry_points={'console_scripts': ['ignr=ignr.cli']},
    packages=['ignr'],
    license='MIT',
    keywords='git gitignore gitignore.io developer'
)