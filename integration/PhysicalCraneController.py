from . import ICraneController

class PhysicalCraneController(ICraneController):
  def reset_crane() -> None:
    raise NotImplementedError

  def rotate_spear(degrees: float) -> None:
    raise NotImplementedError

  def move_appliance(height: float) -> None:
    raise NotImplementedError

  def toggle_electromagnet(state: bool) -> None:
    raise NotImplementedError

  def get_spear_angle() -> float:
    raise NotImplementedError
  
  def get_appliance_height() -> float:
    raise NotImplementedError

  def get_electromagnet_state() -> bool:
    raise NotImplementedError
  
  def get_ultrasonic_distance() -> float:
    raise NotImplementedError