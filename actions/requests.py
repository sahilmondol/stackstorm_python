import requests
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
    def run(self, url):
        print("URL is : {0}".format(url))
		resp = requests.get(url=url)
		data = resp.json()
		print(data)