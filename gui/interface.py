import os
import tkinter as tk
from numpy import var
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from .build_interface import BuildGui
from gui.controller import ControlGui
from functools import partial

PATH = os.path.abspath(os.getcwd())


def create_gui(controller):
    # window = Tk()
    window = ttk.Window(themename="superhero")
    build = BuildGui(window, PATH)
    # controller = ControlGui(controller)

    # Header
    window.title("GUI")
    title = ttk.Label(
        window, text="Guindaste - Protótipo ", anchor="center", font=("Arial Bold", 30)
    )
    title.grid(column=0, columnspan=6, row=0)
    window.iconbitmap(f'{PATH}/gui\/images\/guindaste.ico')
    
    def set_builder(event):
        builder = slider_set.get()
        if builder < 0:
            title["text"] = "Guindaste - Simulação "
        else:
            title["text"] = "Guindaste - Protótipo "
    
    # Slider para escolher entre arduino ou protótipo
    slider_set = build.build_slider_set(set_builder)

    # Controle do atuador de giro do braço
    arm_position, arm_input = build.build_control_arm_gui()

    # Controle do equipamento do braço
    host_position, host_input = build.build_control_hoist_gui()
    
    # Ímã e Sensor de Distância
    ima_value = tk.IntVar()
    sensor_value = build.build_sensor_field()
    
    controller = ControlGui(controller, ima_value, arm_position, arm_input, host_position, host_input, sensor_value)
    
    # controller_ima = partial(controller.set_ima_state, ima_value.get())
    check_ima = tk.Checkbutton(window, text='Ímã', variable=ima_value, command=controller.set_ima_state)
    check_ima.grid(padx=10, pady=10, column=20, row=4)
    
    # Buttons
    btn_exe_gui = ttk.Button(
        window, text="Exec", command=controller.command_move_appliance, bootstyle=SUCCESS
    )
    btn_exe_gui.grid(column=3, row=10)
    
    btn_alert = ttk.Button(
        window, text="Reset", command=controller.reset_values, bootstyle=SECONDARY
    )
    btn_alert.grid(column=9, row=10)

    return window
