import os
import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from .build_interface import BuildGui
from gui.controller import ControlGui


PATH = os.path.abspath(os.getcwd())


def create_gui():
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
    arm_position, arm_input, arm_input_to = build.build_control_arm_gui(row=2, column=0) # Row até 5
    
    # Controle do equipamento do braço
    host_position, host_input, host_input_to = build.build_control_hoist_gui(row=2, column=9)

    # Ímã e Sensor de Distância
    ima_value = tk.IntVar()
    sensor_value = build.build_sensor_field()
    
    controller = ControlGui(ima_value, arm_position, arm_input, 
                            host_position, host_input, 
                            sensor_value, slider_set, title,
                            arm_input_to, host_input_to)
    
    # controller_ima = partial(controller.set_ima_state, ima_value.get())
    check_ima = ttk.Checkbutton(window, text='Ímã', variable=ima_value, command=controller.set_ima_state, bootstyle="success")
    check_ima.grid(padx=10, pady=10, column=20, row=4)
    
    # Buttons Moviments
    btn_arm_left = ttk.Button(
        window, text="⬇", command=controller.move_appliance_left, bootstyle="primary-outline"
    )
    btn_arm_left.grid(column=0, row=5)
    btn_arm_right = ttk.Button(
        window, text="⬆", command=controller.move_appliance_right, bootstyle="primary-outline"
    )
    btn_arm_right.grid(column=1, row=5)
    
    btn_spear_down = ttk.Button(
        window, text="⬅", command=controller.move_spear_down, bootstyle="primary-outline"
    )
    btn_spear_down.grid(column=9, row=5)
    btn_spear_up = ttk.Button(
        window, text="➡", command=controller.move_spear_up, bootstyle="primary-outline"
    )
    btn_spear_up.grid(column=10, row=5)
    
    # Buttons Executions
    btn_move_appliance = ttk.Button(
        window, text="Move Appliance", command=controller.command_move_appliance, bootstyle=SUCCESS
    )
    btn_move_appliance.grid(column=0, row=10)
    btn_move_appliance_to = ttk.Button(
        window, text="Move Appliance To", command=controller.command_move_appliance_to, bootstyle=SUCCESS
    )
    btn_move_appliance_to.grid(column=1, row=10)
    
    btn_rotate_spear = ttk.Button(
        window, text="Rotate Spear", command=controller.command_move_spear, bootstyle=SUCCESS
    )
    btn_rotate_spear.grid(column=9, row=10)
    btn_rotate_spear_to = ttk.Button(
        window, text="Rotate Spear", command=controller.command_move_spear_to, bootstyle=SUCCESS
    )
    btn_rotate_spear_to.grid(column=10, row=10)
    
    btn_alert = ttk.Button(
        window, text="Reset", command=controller.reset_values, bootstyle=SECONDARY
    )
    btn_alert.grid(column=12, row=10)

    return window


# TODO Adicionar 40 menos o sensor na GUI
# TODO adicionar negocio de pra onde quer mandar o guindates