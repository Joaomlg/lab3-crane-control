import os
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from .build_interface import BuildGui

PATH = os.path.abspath(os.getcwd())


def create_gui(controller):
    # window = Tk()
    window = ttk.Window(themename="superhero")
    build = BuildGui(window, PATH)

    # Header
    window.title("GUI")
    title = ttk.Label(
        window, text="Guindaste", anchor="center", font=("Arial Bold", 30)
    )
    title.grid(column=0, columnspan=12, row=0)

    # Controle do atuador de giro do braço
    build.build_control_arm_gui()

    # Controle do equipamento do braço
    build.build_control_hoist_gui()

    btn_exe_gui = ttk.Button(
        window, text="Exec", command=controller.move_appliance(0), bootstyle=SUCCESS
    )
    btn_exe_gui.grid(column=3, row=10)
    btn_alert = ttk.Button(
        window, text="Reset", command=controller.reset_crane(), bootstyle=SECONDARY
    )
    btn_alert.grid(column=9, row=10)

    return window
