from distutils.core import setup

setup(
    name='gitignoreio_py',
    description='Python command line client to access' \
                '.gitignore templates from gitignore.io',
    version='1.0',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    packages=['gitignoreio'],
    scripts=['bin/cli.py'],
    # url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.md'
)