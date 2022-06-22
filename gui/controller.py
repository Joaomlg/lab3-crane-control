from tkinter import *


class ControlGui:
    def __init__(self, controller, ima_value, arm_position, arm_input, hoist_position, hoist_input, sensor_value):
        self.controller = controller
        self.ima_value = ima_value
        self.arm_position = arm_position
        self.arm_input = arm_input
        self.hoist_position = hoist_position
        self.hoist_input = hoist_input
        self.sensor_value = sensor_value

    def command_move_appliance(self):
        self.controller.move_appliance(self.arm_input.get())
        self.controller.rotate_spear(self.hoist_input.get())
        self.update_field_values()
    
    def update_field_values(self):
        self.arm_position["text"] = self.controller.get_appliance_height()
        self.hoist_position["text"] = self.controller.get_spear_angle()
        self.sensor_value["text"] = self.controller.get_ultrasonic_distance()

    def reset_values(self):
        self.controller.reset_crane()

        # GUI Values
        self.hoist_input.delete(0,END)
        self.hoist_input.insert(0, "0")
        self.arm_input.delete(0,END)
        self.arm_input.insert(0, "0")
        return

    def set_ima_state(self):
        self.controller.toggle_electromagnet(self.ima_value.get())
        return
