import sys

from st2common.runners.base_action import Action

class Greet(Action):
    def run(self, message, country):
        print("Welcome {0}, to StackStorm!!!!".format(message))
        print("And You're from {0}..".format(country))

