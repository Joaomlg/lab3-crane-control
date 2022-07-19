import time
import threading

from tkinter import *
from integration.CraneControllerFactory import CraneControllerFactory, Variant


class ControlGui:
    def __init__(self, ima_value, arm_position, arm_input, hoist_position, hoist_input, 
                 sensor_value, slider_set, title, arm_input_to, host_input_to, object_height):
        # self.controller_physical = CraneControllerFactory.create(Variant.Temporary)
        self.controller_physical = CraneControllerFactory.create(Variant.Physical)
        self.controller_simulation = CraneControllerFactory.create(Variant.Temporary)
        # self.controller_simulation = CraneControllerFactory.create(Variant.Simulation)

        self.ima_value = ima_value
        self.arm_position = arm_position
        self.arm_input = arm_input
        self.hoist_position = hoist_position
        self.hoist_input = hoist_input
        self.sensor_value = sensor_value
        self.slider_set = slider_set
        self.title = title
        self.arm_input_to = arm_input_to 
        self.host_input_to = host_input_to
        self.object_height = object_height
        # slider_set.configure(command= self.update_field_values)

        existsThread = next((thread for thread in threading.enumerate() if thread.name == 'thread_update_values'), False)
        if existsThread == False:
            radioThread = threading.Thread(target = self.update_field_values, daemon=True, name="thread_update_values")
            radioThread.start()

    def get_controller(self):
        if self.slider_set.get() < 0:
            self.title["text"] = "Guindaste - Simulação "
            return self.controller_simulation
        self.title["text"] = "Guindaste - Protótipo "
        return self.controller_physical

    def command_move_appliance(self):
        controller = self.get_controller()
        controller.move_appliance(self.arm_input.get())
    
    def command_move_appliance_to(self):
        controller = self.get_controller()
        controller.move_appliance(float(self.arm_input_to.get()) - float(controller.get_appliance_height()))

    def command_move_spear_to(self):
        controller = self.get_controller()
        controller.rotate_spear(float(self.host_input_to.get()) - float(controller.get_spear_angle()))

    def command_move_spear(self):
        controller = self.get_controller()
        controller.rotate_spear(self.hoist_input.get())
        # self.update_field_values()     
    
    def update_field_values(self, event=None):
        while True:
            time.sleep(1)
            controller = self.get_controller()
            self.arm_position["text"] = controller.get_appliance_height()
            self.hoist_position["text"] = controller.get_spear_angle()
            self.sensor_value["text"] = controller.get_ultrasonic_distance()
            self.object_height["text"] = 40 - float(controller.get_ultrasonic_distance())
        # self.reset_values()

    def reset_values(self):
        controller = self.get_controller()
        controller.reset_crane()

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
        # self.update_field_values()
    
    def move_appliance_left(self):
        controller = self.get_controller()
        controller.move_appliance(-1)
        # self.update_field_values()

    def move_spear_up(self):
        controller = self.get_controller()
        controller.rotate_spear(1)
        # self.update_field_values()

    def move_spear_down(self):
        controller = self.get_controller()
        controller.rotate_spear(-1)
        # self.update_field_values()
