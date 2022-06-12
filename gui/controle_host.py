import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from PIL import ImageTk, Image  


def build_control_host_gui(window, ):
    title = ttk.Label(window, text="Host Scale", anchor='center', font=("Arial Bold", 15))
    title.grid(column=9, row=2, columnspan=4)
    
    img_hoist = Image.open(path_images+"/gui\/images\/hoist.png")
    img_hoist = img_hoist.resize((250, 250), Image.ANTIALIAS)
    img_hoist = ImageTk.PhotoImage(img_hoist)
    panel = ttk.Label(window, image=img_hoist)
    panel.image = img_hoist
    panel.grid(column=9, columnspan=4, row=3)
    
    ttk.Label(window, text="Hoist Steps").grid(column=9, row=4)
    host_input = ttk.Entry(window, width=10)
    host_input.grid(padx=10, pady=10, column=10, row=4)