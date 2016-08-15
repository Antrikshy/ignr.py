import requests

def get_template_list():
    response = requests.get('https://api.github.com/events')
    print response
