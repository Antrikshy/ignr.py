#! /usr/bin/env python

import argparse, sys
sys.path.append('../gitignoreio.py')
import gitignoreio

def msg(name=None):                                                            
    return '''
    
    ignr [-h] (--list | --new TECH [TECH ...] [--preview])

          Python-based CLI tool for gitignore.io

    --help,    -h             show this message and exit
    --list,    -l             list all available .gitignore templates
    --new,     -n TECH ...    space-separated list of technologies to include
    --preview, -p             (use with --new ) preview .gitignore contents
    '''

parser = argparse.ArgumentParser(usage=msg())

# Accept list instruction, search instruction, OR create instruction
list_or_search = parser.add_mutually_exclusive_group(required=True)
list_or_search.add_argument('--list', '-l', action='store_true')
list_or_search.add_argument('--new', '-n', dest='gi_stack', metavar='TECH', nargs='+')
# Optional output preview flag (manually checked)
parser.add_argument('--preview', '-p', action='store_true')

args = parser.parse_args()

if args.list:
    pass

elif args.new:
    pass
