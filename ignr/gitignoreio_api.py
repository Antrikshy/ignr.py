from urllib import request

headers = {'User-Agent': 'ignr.py'}

BASE_URL = 'https://donotcommit.com'


class GitignoreIOAPI:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def request(self, url):
        return request.urlopen(
            request.Request(self.base_url + url, headers=headers)
        ).read().decode('utf-8')
    
    def get_template_list(self):
        response = self.request('/api/list')
        
        template_list = []
        for line in map(str, response.split('\n')):
            template_list.extend(line.split(','))

        return template_list

    def get_gitignore(self, gi_stack):
        template_list = self.get_template_list()

        for tech in gi_stack:
            if tech.lower() not in template_list:
                raise ValueError(tech)  # Reports iffy item in the list

        comma_delimited = ','.join(gi_stack)
        response = self.request('/api/' + comma_delimited)

        return response
