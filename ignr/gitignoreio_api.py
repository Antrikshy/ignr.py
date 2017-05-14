import urllib2
import os
from os import path


def cache_template_list(template_list):
    ignr_home = path.expanduser("~/.ignr")

    if not path.exists(ignr_home):
        os.mkdir(ignr_home)

    with file(path.join(ignr_home, "template_list.txt"), "w") as fp:
        fp.write("\n".join(template_list))


def read_cache_template_list():
    from os import path
    cached = path.expanduser("~/.ignr/template_list.txt")

    if path.exists(cached):
        with file(cached) as fp:
            template_list = fp.read().splitlines()
        return template_list

    return None


def get_template_list(force=True):
    template_list = read_cache_template_list()

    if not template_list or force:
        response = urllib2.urlopen('https://www.gitignore.io/api/list').read()
        template_list = []

        for line in map(str, response.split('\n')):
            template_list.extend(line.split(','))

        cache_template_list(template_list)

    return template_list


# gi_stack is a list of strings of names of tech to include
# ex. ['sass', 'node', 'macos']
def get_gitignore(gi_stack):
    template_list = get_template_list()

    for tech in gi_stack:
        if tech.lower() not in template_list:
            raise ValueError(tech)  # Reports iffy item in the list

    comma_delimited = ','.join(gi_stack)
    response = urllib2.urlopen('https://www.gitignore.io/api/' + comma_delimited).read()

    return response
