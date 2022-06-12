import os
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from .control_arm import build_control_arm_gui
from .controle_host import build_control_host_gui

PATH = os.path.abspath(os.getcwd())

def create_gui():
    # window = Tk()
    window = ttk.Window(themename="superhero")

    # Header
    window.title("GUI")
    title = ttk.Label(window, text="Guindaste", anchor='center', font=("Arial Bold", 30))
    title.grid(column=0, columnspan=12, row=0)

    # Controle do atuador de giro do braço
    build_control_arm_gui(window, PATH)
    
    # Controle do equipamento do braço
    build_control_host_gui(window, PATH)

    def reset_values():
        pass
    def get_value_input():
        pass
        
    btn_exe_gui = ttk.Button(window, text='Exec', command=get_value_input, bootstyle=SUCCESS)
    btn_exe_gui.grid(column=3, row=6)
    btn_alert = ttk.Button(window, text='Reset', command=reset_values,bootstyle=SECONDARY)
    btn_alert.grid(column=9, row=6)
    
    return window
