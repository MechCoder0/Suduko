class Controller:
    def __init__(self) -> None:
        self.actions = {}

    def get_action(self, event):
        result = self.actions.get(event.type)
        if result:
            if hasattr(event, "key"):
                result = result.get(event.key)

        return result
    

    def run_action(self, events, approved_actions=[]):
        for event in events:
            action = self.get_action(event)
            if action and action in approved_actions:
                action()