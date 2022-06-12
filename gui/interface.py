import os
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import ImageTk, Image  


PATH = os.path.abspath(os.getcwd())

def create_gui():
    # window = Tk()
    window = ttk.Window(themename="superhero")

    # Header
    window.title("GUI")
    title = ttk.Label(window, text="Guindaste", anchor='center', font=("Arial Bold", 30))
    title.grid(column=0, columnspan=12, row=0)

    # Controle do atuador de giro do braço
    title = ttk.Label(window, text="Arm Scale", anchor='center', font=("Arial Bold", 15))
    title.grid(column=0, row=2, columnspan=4)
    
    img_arm = Image.open(PATH+"/gui\/images\/arm.png")
    img_arm = img_arm.resize((250, 250), Image.ANTIALIAS)
    img_arm = ImageTk.PhotoImage(img_arm)
    panel = ttk.Label(window, image=img_arm)
    panel.image = img_arm
    panel.grid(column=0, columnspan=4, row=3)
    
    ttk.Label(window, text="Arm Rotate Degrees").grid(column=0, row=4)
    arm_input = ttk.Entry(window, width=10)
    arm_input.grid(padx=10, pady=10, column=1, row=4)

    # Controle do equipamento do braço
    title = ttk.Label(window, text="Host Scale", anchor='center', font=("Arial Bold", 15))
    title.grid(column=9, row=2, columnspan=4)
    
    img_hoist = Image.open(PATH+"/gui\/images\/hoist.png")
    img_hoist = img_hoist.resize((250, 250), Image.ANTIALIAS)
    img_hoist = ImageTk.PhotoImage(img_hoist)
    panel = ttk.Label(window, image=img_hoist)
    panel.image = img_hoist
    panel.grid(column=9, columnspan=4, row=3)
    
    ttk.Label(window, text="Hoist Steps").grid(column=9, row=4)
    host_input = ttk.Entry(window, width=10)
    host_input.grid(padx=10, pady=10, column=10, row=4)

    def reset_values():
        pass
    def get_value_input():
        pass
        
    btn_exe_gui = ttk.Button(window, text='Exec', command=get_value_input, bootstyle=SUCCESS)
    btn_exe_gui.grid(column=3, row=6)
    btn_alert = ttk.Button(window, text='Reset', command=reset_values,bootstyle=SECONDARY)
    btn_alert.grid(column=9, row=6)
    
    return window
