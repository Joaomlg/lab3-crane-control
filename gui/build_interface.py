import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import ImageTk, Image


class BuildGui:
    def __init__(self, window, PATH):
        self.window = window
        self.PATH = PATH


    def build_control_arm_gui(self, row=2, column=0):
        title = ttk.Label(
            self.window, text="Arm Scale", anchor="center", font=("Arial Bold", 15)
        )
        title.grid(column=column, row=row, columnspan=4)

        img_arm = Image.open(self.PATH + "/gui\/images\/hoist.png")
        img_arm = img_arm.resize((250, 250), Image.ANTIALIAS)
        img_arm = ImageTk.PhotoImage(img_arm)
        panel = ttk.Label(self.window, image=img_arm)
        panel.image = img_arm
        panel.grid(column=column, row=row+1, columnspan=4)
        
        # Show degress
        ttk.Label(self.window, text="Curret Position").grid(column=column, row=row+2)
        arm_position = ttk.Label(
            self.window, text="0", anchor="center", font=("Arial Bold", 12)
        )
        arm_position.grid(padx=10, pady=10, column=column+1, row=row+2)
        
        # Input degress
        ttk.Label(self.window, text="Move Appliance").grid(column=column, row=row+4)
        arm_input = ttk.Entry(self.window, width=10)
        arm_input.grid(padx=10, pady=10, column=column+1, row=row+4)
        arm_input.insert(0, 0)
        
        # Input degress TO
        ttk.Label(self.window, text="Move Appliance To").grid(column=column, row=row+5)
        arm_input_to = ttk.Entry(self.window, width=10)
        arm_input_to.grid(padx=10, pady=10, column=column+1, row=row+5)
        arm_input_to.insert(0, 0)
        
        return arm_position, arm_input, arm_input_to

    def build_control_hoist_gui(self, row=2, column=9):
        title = ttk.Label(
            self.window, text="Hoist Scale", anchor="center", font=("Arial Bold", 15)
        )
        title.grid(column=column, row=row, columnspan=4)

        img_hoist = Image.open(self.PATH + "/gui\/images\/arm.png")
        img_hoist = img_hoist.resize((250, 250), Image.ANTIALIAS)
        img_hoist = ImageTk.PhotoImage(img_hoist)
        panel = ttk.Label(self.window, image=img_hoist)
        panel.image = img_hoist
        panel.grid(column=column, row=row+1, columnspan=4)

        # Show degress
        ttk.Label(self.window, text="Curret Position").grid(column=column, row=row+2)
        host_position = ttk.Label(
            self.window, text="0", anchor="center", font=("Arial Bold", 12)
        )
        host_position.grid(padx=10, pady=10, column=column+1, row=row+2)

        # Input degress
        ttk.Label(self.window, text="Arm Degrees").grid(column=column, row=row+4)
        host_input = ttk.Entry(self.window, width=10)
        host_input.insert(0, 0)
        host_input.grid(padx=10, pady=10, column=column+1, row=row+4)
        
        ttk.Label(self.window, text="Arm Degrees To").grid(column=column, row=row+5)
        host_input_to = ttk.Entry(self.window, width=10)
        host_input_to.insert(0, 0)
        host_input_to.grid(padx=10, pady=10, column=column+1, row=row+5)
        
        return host_position, host_input, host_input_to

    def build_slider_set(self, set_builder):
        ttk.Label(self.window, text="Simulação").grid(column=7, row=0)
        slider_set = ttk.Scale(self.window, from_=-1, to=1, orient=HORIZONTAL, command=set_builder)
        slider_set.grid(column=8, columnspan=4, row=0)
        ttk.Label(self.window, text="Protótipo").grid(column=12, row=0)
        
        return slider_set
    
    def build_sensor_field(self):
        ttk.Label(self.window, text="Sensor").grid(column=18, row=5)
        sensor_value = ttk.Label(
            self.window, text="0", anchor="center", font=("Arial Bold", 12)
        )
        sensor_value.grid(padx=10, pady=10, column=20, row=5)
        
        ttk.Label(self.window, text="Altura do objeto").grid(column=18, row=6)
        object_height = ttk.Label(
            self.window, text="0", anchor="center", font=("Arial Bold", 12)
        )
        object_height.grid(padx=10, pady=10, column=20, row=6)
        
        return sensor_value, object_height
