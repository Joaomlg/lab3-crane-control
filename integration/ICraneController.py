from abc import ABC, abstractmethod

class ICraneController(ABC):
  @abstractmethod
  def reset_crane(self) -> None:
    raise NotImplementedError

  @abstractmethod
  def rotate_spear(self, degrees: float) -> None:
    raise NotImplementedError

  @abstractmethod
  def move_appliance(self, height: float) -> None:
    raise NotImplementedError

  @abstractmethod
  def toggle_electromagnet(self, state: bool) -> None:
    raise NotImplementedError

  @abstractmethod
  def get_spear_angle(self) -> float:
    raise NotImplementedError
  
  @abstractmethod
  def get_appliance_height(self) -> float:
    raise NotImplementedError

  @abstractmethod
  def get_electromagnet_state(self) -> bool:
    raise NotImplementedError
  
  @abstractmethod
  def get_ultrasonic_distance(self) -> float:
    raise NotImplementedError