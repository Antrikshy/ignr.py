# ignr.py

ignr.py (or simply ignr) is a Python-based command line utility to fetch .gitignore templates from [gitignore.io](https://gitignore.io). gitignore.io has official [command line tools](https://github.com/joeblau/gitignore.io#install-command-line), but they rely on bash or zsh, and *may* not be compatible with all systems out there.

There's also a Go-based alternative, [gogi](https://github.com/Gnouc/gogi), but not everyone uses Go.

ignr was created for Python users who prefer to install via [PyPI](https://pypi.python.org/pypi) and/or [pip](https://pip.pypa.io).

Python 2 support was fully dropped in favor of Python 3 in version 2.0, released in late 2019.

## Usage

Install using
    
    pip install ignr

### List

    ignr -l

Lists all available .gitignore templates on gitignore.io.

### Search

    ignr -s mac

Searches for supplied query in list of available templates from gitignore.io, similar to using `grep`.

### Preview

    ignr -p scala macOS

Prints a preview of the template without generating a .gitignore file. List multiple space-separated languages, frameworks, operating systems to get combined output.

### Create

    ignr -n node sass windows

Generates a new .gitignore file in the current directory. List multiple space-separated languages, frameworks, operating systems to get combined output.

If a .gitignore already exists in the directory, ignr will give you an option to back it up.

## Troubleshooting

Since gitignore.io uses HTTPS, running this utility in certain macOS environments may result in an SSL "handshake failure" error, which is discussed in detail in this [requests issue](https://github.com/kennethreitz/requests/issues/2022).

Unfortunately, there is no trivial fix.

In my experience, switching from the included Python in El Capitan to a standalone Python installed via brew solved the issue. All my existing packages seemed to remain intact.

## Contribute

Feel free to make improvements. PRs are greatly appreciated. ignr is currently untested on Windows. If you can confirm that it works, please let me know. You can open a PR to edit this line out if you want. If not, fixes would be nice.

I can be reached [@Antrikshy](https://twitter.com/Antrikshy) or [via reddit](https://www.reddit.com/u/Antrikshy).