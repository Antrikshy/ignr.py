# ignr.py

ignr.py (or simply ignr) is a Python-based command line utility to fetch .gitignore templates. It currently sources .gitignore files from [Do Not Commit](https://donotcommit.com).

ignr was originally written as a client for [gitignore.io](https://gitignore.io), before that service appeared to be deprecated (see [PR #6](https://github.com/Antrikshy/ignr.py/pull/6)).

Do Not Commit and gitignore.io have other clients. ignr was created for Python users who prefer to install via [PyPI](https://pypi.python.org/pypi) and [pip](https://pip.pypa.io).

The .gitignore file in this repository was generated using ignr, if you want to look at a sample!

> Note: Version 2.0 completely drops Python 2 support in favor of Python 3, released late-2019.

## Usage

Install using pip3, or consider using [pipx](https://pipx.pypa.io) to keep things clean.

    pip3 install ignr

    // OR

    <install pipx>
    pipx install ignr

### List

    ignr -l

Lists all available .gitignore templates.

### Search

    ignr -s mac

Searches for supplied query in list of available templates, similar to using `grep`.

### Preview

    ignr -p scala macOS

Prints a preview of the template without generating a .gitignore file. List multiple space-separated languages, frameworks, operating systems to get combined output.

### Create

    ignr -n node sass windows

Generates a new .gitignore file in the current directory. List multiple space-separated languages, frameworks, operating systems to get combined output.

If a .gitignore already exists in the directory, ignr will give you an option to back it up.

## Contribute

Feel free to make improvements. PRs are greatly appreciated.

I can be reached [via Reddit Chat](https://www.reddit.com/u/Antrikshy).
