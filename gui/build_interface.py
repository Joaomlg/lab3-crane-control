import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import ImageTk, Image


class BuildGui:
    def __init__(self, window, PATH):
        self.window = window
        self.PATH = PATH

    def build_control_arm_gui(self):
        title = ttk.Label(
            self.window, text="Arm Scale", anchor="center", font=("Arial Bold", 15)
        )
        title.grid(column=0, row=2, columnspan=4)

        img_arm = Image.open(self.PATH + "/gui\/images\/arm.png")
        img_arm = img_arm.resize((250, 250), Image.ANTIALIAS)
        img_arm = ImageTk.PhotoImage(img_arm)
        panel = ttk.Label(self.window, image=img_arm)
        panel.image = img_arm
        panel.grid(column=0, columnspan=4, row=3)
        
        # Show degress
        ttk.Label(self.window, text="Curret Position").grid(column=0, row=4)
        arm_position = ttk.Entry(self.window, width=10, state="disabled")
        arm_position.grid(padx=10, pady=10, column=1, row=4)
        
        # Input degress
        ttk.Label(self.window, text="Arm Rotate Degrees").grid(column=0, row=5)
        arm_input = ttk.Entry(self.window, width=10)
        arm_input.grid(padx=10, pady=10, column=1, row=5)


    def build_control_hoist_gui(self):
        title = ttk.Label(
            self.window, text="Hoist Scale", anchor="center", font=("Arial Bold", 15)
        )
        title.grid(column=9, row=2, columnspan=4)

        img_hoist = Image.open(self.PATH + "/gui\/images\/hoist.png")
        img_hoist = img_hoist.resize((250, 250), Image.ANTIALIAS)
        img_hoist = ImageTk.PhotoImage(img_hoist)
        panel = ttk.Label(self.window, image=img_hoist)
        panel.image = img_hoist
        panel.grid(column=9, columnspan=4, row=3)

        # Show degress
        ttk.Label(self.window, text="Curret Position").grid(column=9, row=4)
        host_position = ttk.Entry(self.window, width=10, state="disabled")
        host_position.grid(padx=10, pady=10, column=10, row=4)
        
        # Input degress
        ttk.Label(self.window, text="Hoist Steps").grid(column=9, row=5)
        host_input = ttk.Entry(self.window, width=10)
        host_input.grid(padx=10, pady=10, column=10, row=5)