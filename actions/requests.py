import urllib
import json
import sys

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,message):
        print(json.load(urllib.urlopen(url)))