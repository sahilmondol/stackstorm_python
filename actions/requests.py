import requests
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self):
		temp_url = "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json"
        req = requests.get(temp_url)
        template = req.json()
        print(template)