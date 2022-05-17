from integration.ICraneController import ICraneController
from utils.SingletonMetaClass import AbstractSingletonMetaClass

class PhysicalCraneController(ICraneController, metaclass=AbstractSingletonMetaClass):
  def __init__(self):
    pass

  def reset_crane(self) -> None:
    raise NotImplementedError

  def rotate_spear(self, degrees: float) -> None:
    raise NotImplementedError

  def move_appliance(self, height: float) -> None:
    raise NotImplementedError

  def toggle_electromagnet(self, state: bool) -> None:
    raise NotImplementedError

  def get_spear_angle(self) -> float:
    raise NotImplementedError
  
  def get_appliance_height(self) -> float:
    raise NotImplementedError

  def get_electromagnet_state(self) -> bool:
    raise NotImplementedError
  
  def get_ultrasonic_distance(self) -> float:
    raise NotImplementedError