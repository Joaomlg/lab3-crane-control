import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import ImageTk, Image  


def build_control_arm_gui(window, path_images):
    title = ttk.Label(window, text="Arm Scale", anchor='center', font=("Arial Bold", 15))
    title.grid(column=0, row=2, columnspan=4)

    img_arm = Image.open(path_images+"/gui\/images\/arm.png")
    img_arm = img_arm.resize((250, 250), Image.ANTIALIAS)
    img_arm = ImageTk.PhotoImage(img_arm)
    panel = ttk.Label(window, image=img_arm)
    panel.image = img_arm
    panel.grid(column=0, columnspan=4, row=3)

    ttk.Label(window, text="Arm Rotate Degrees").grid(column=0, row=4)
    arm_input = ttk.Entry(window, width=10)
    arm_input.grid(padx=10, pady=10, column=1, row=4)
