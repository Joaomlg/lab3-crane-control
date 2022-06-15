

class ControlGui:
    def __init__(self, controller):
        self.controller = controller

    def command_move_appliance(self):
        self.controller.move_appliance(0)

    def reset_values(self):
        return