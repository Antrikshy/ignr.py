from setuptools import setup

setup(
    name='ignr',
    description='Python command line client to download' \
                '.gitignore templates from gitignore.io',
    version='2.2',
    url='https://github.com/Antrikshy/ignr',
    author='Antriksh Yadav',
    author_email='antrikshy@gmail.com',
    entry_points={'console_scripts': ['ignr=ignr.cli:__main__']},
    packages=['ignr'],
    license='MIT',
    keywords='git gitignore gitignore.io developer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git'
    ]
)