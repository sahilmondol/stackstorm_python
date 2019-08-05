import urllib
import json
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,message):
		#url="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json"
		print(json.load(urllib.urlopen(message)))