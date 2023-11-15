from pygame import quit
from pygame.event import get
from sys import exit

class Controller:
    def __init__(self) -> None:
        self.actions = {}

    def get_action(self, event):
        result = self.actions.get(event.type)
        if result:
            if hasattr(event, "key"):
                result = result.get(event.key)

        return result
    

    def run_action(self, approved_actions=[]):
        events = get()
        for event in events:
            action = self.get_action(event)
            if action and action in approved_actions:
                self.event = event
                action()
    
    def quit(self):
        print("Quitting the game.")
        quit()
        exit()