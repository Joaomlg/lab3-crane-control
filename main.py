from msilib.schema import ControlEvent
from integration.CraneControllerFactory import CraneControllerFactory, Variant
from gui.interface import create_gui

controller = CraneControllerFactory.create(Variant.Temporary)

# while True:
#     degrees = float(input("> "))
#     controller.rotate_spear(3.33 * degrees)
    
if __name__ == '__main__':
    # sim.startSimulation()
    window = create_gui(controller)
    window.mainloop()