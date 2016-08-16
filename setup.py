from distutils.core import setup

setup(
    name='ignr.py',
    description='Python command line client to download' \
                '.gitignore templates from gitignore.io',
    version='1.0',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    scripts=['bin/ignr'],
    py_modules=['gitignoreio_api'],
    license='LICENSE.md'
)