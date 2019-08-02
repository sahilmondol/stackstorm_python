import sys

from st2common.runners.base_action import Action

class Greet(Action):
    def run(self, message):
        print(output)
		output = "Welcome" + message
		print(output)