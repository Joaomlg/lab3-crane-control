from tkinter import *


class ControlGui:
    def __init__(self, controller):
        self.controller = controller

    def command_move_appliance(self):
        self.controller.move_appliance(0)

    def reset_values(self, hoist_input, arm_input):
        self.controller.reset_crane()
        
        # GUI Values
        hoist_input.delete(0,END)
        hoist_input.insert(0, "0")
        arm_input.delete(0,END)
        arm_input.insert(0, "0")
        return

    def set_ima_state(self, state):
        self.controller.toggle_electromagnet(state)
        return
