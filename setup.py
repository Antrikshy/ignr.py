from distutils.core import setup

setup(
    name='ignr',
    description='Python command line client to download' \
                '.gitignore templates from gitignore.io',
    version='1.0',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    scripts=['ignr.py'],
    py_modules=['gitignoreio_api'],
    license='LICENSE.md'
)