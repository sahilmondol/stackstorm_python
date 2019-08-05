import requests
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self, message):
		print("URL is : {0}".format(message))
		resp = requests.get(message)
		data = resp.json()		        
		print(data)