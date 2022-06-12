

class ControlGui:
    def __init__(self, controller):
        self.controller = controller

    def button_set_values(self):
        self.controller.move_appliance(0)
