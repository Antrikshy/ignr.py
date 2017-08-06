try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def get_template_list():
    response = urlopen('https://www.gitignore.io/api/list').read().decode()
    template_list = []

    for line in response.split('\n'):
        template_list.extend(line.split(','))

    return template_list


# gi_stack is a list of strings of names of tech to include
# ex. ['sass', 'node', 'macos']
def get_gitignore(gi_stack):
    template_list = get_template_list()

    for tech in gi_stack:
        if tech.lower() not in template_list:
            raise ValueError(tech)  # Reports iffy item in the list

    comma_delimited = ','.join(gi_stack)
    response = urlopen('https://www.gitignore.io/api/' + comma_delimited).read().decode()

    return response
