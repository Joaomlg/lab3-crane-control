from tkinter import *
from integration.CraneControllerFactory import CraneControllerFactory, Variant


class ControlGui:
    def __init__(self, ima_value, arm_position, arm_input, hoist_position, hoist_input, sensor_value, slider_set):
        self.controller_physical = CraneControllerFactory.create(Variant.Temporary)
        # self.controller_physical = CraneControllerFactory.create(Variant.Physical)
        self.controller_simulation = CraneControllerFactory.create(Variant.Temporary)
        # self.controller_simulation = CraneControllerFactory.create(Variant.Simulation)

        self.ima_value = ima_value
        self.arm_position = arm_position
        self.arm_input = arm_input
        self.hoist_position = hoist_position
        self.hoist_input = hoist_input
        self.sensor_value = sensor_value
        self.slider_set = slider_set

    def get_controller(self):
        if self.slider_set.get() < 0:
            return self.controller_physical
        return self.controller_simulation

    def command_move_appliance(self):
        controller = self.get_controller()
        controller.move_appliance(self.arm_input.get())
        controller.rotate_spear(self.hoist_input.get())
        self.update_field_values()
    
    def update_field_values(self):
        controller = self.get_controller()
        self.arm_position["text"] = controller.get_appliance_height()
        self.hoist_position["text"] = controller.get_spear_angle()
        self.sensor_value["text"] = controller.get_ultrasonic_distance()
        # self.reset_values()

    def reset_values(self):
        controller = self.get_controller()
        controller.reset_crane()
        self.update_field_values()

        # GUI Values
        self.hoist_input.delete(0,END)
        self.hoist_input.insert(0, "0")
        self.arm_input.delete(0,END)
        self.arm_input.insert(0, "0")
        return

    def set_ima_state(self):
        controller = self.get_controller()
        controller.toggle_electromagnet(self.ima_value.get())
        return

    def move_appliance_right(self):
        controller = self.get_controller()
        controller.move_appliance(1)
        self.update_field_values()
    
    def move_appliance_left(self):
        controller = self.get_controller()
        controller.move_appliance(-1)
        self.update_field_values()

    def move_spear_up(self):
        controller = self.get_controller()
        controller.rotate_spear(1)
        self.update_field_values()

    def move_spear_down(self):
        controller = self.get_controller()
        controller.rotate_spear(-1)
        self.update_field_values()