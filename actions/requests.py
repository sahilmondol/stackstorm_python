import urllib
import json
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,message):
		result = json.load(urllib.urlopen(url))
        print(result)