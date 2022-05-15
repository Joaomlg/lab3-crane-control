from abc import ABC, abstractmethod

class ICraneController(ABC):
  @abstractmethod
  def rotate_spear(degrees: float) -> None:
    raise NotImplementedError

  @abstractmethod
  def move_appliance(height: float) -> None:
    raise NotImplementedError

  @abstractmethod
  def toggle_electromagnet(state: bool) -> None:
    raise NotImplementedError

  @abstractmethod
  def get_spear_angle() -> float:
    raise NotImplementedError
  
  @abstractmethod
  def get_appliance_height() -> float:
    raise NotImplementedError

  @abstractmethod
  def get_electromagnet_state() -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def get_ultrasonic_distance() -> float:
    raise NotImplementedError