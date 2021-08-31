from pprint import pprint

import requests

# token = '2619421814940190'
API_BASE_URL = ' https://superheroapi.com/api/2619421814940190/'
# headers = {'accept': 'application/json', 'authorization': f'OAuth {token}'}
# superhero_list = ['Hulk', 'Captain America', 'Thanos']
superhero_dict = {}


class SuperheroID():
    def __init__(self, name):
        self.name = name
        self.response = requests.get(API_BASE_URL + 'search/' + self.name)
        self.id = self.response.json()['results'][0]['id']
        self.response = requests.get(API_BASE_URL + self.id)
        self.intelligence = self.response.json()['powerstats']['intelligence']
        # print(self.intelligence)
        superhero_dict[self.name] = self.intelligence
        return

Hulk = SuperheroID('Hulk')
Captain_America = SuperheroID('Captain America')
Thanos = SuperheroID('Thanos')
print(superhero_dict)
sh_intelligence = 0
sh_name = 0
for name, intel in superhero_dict.items():
    if int(intel) > sh_intelligence:
        sh_intelligence = int(intel)
        sh_name = name
    else:
        pass

print(f'Самый умный из указанных супергероев:{sh_name}, его ум:{sh_intelligence}')

