import urllib
import json
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,message):
		#temp_url = "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json"
        #req = requests.get('https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json')
        #template = req.json()
        result = json.load(urllib.urlopen(url))
        print(result)