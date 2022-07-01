from abc import ABC, abstractmethod

class TempICraneController(ABC):
  def __init__(self) -> None:
    super().__init__()
    self.current_ultrassonic = 0
    self.current_degress = 0
    self.current_height = 0
    self.current_eletric_state = False
  
  def reset_crane(self) -> None:
    self.current_degress = 0
    self.current_height = 0
    print("All values to 0")

  def rotate_spear(self, degrees: float) -> None:
    self.current_degress += float(degrees)
    print("> Rotating spear by " + str(degrees) + " degrees")

  def move_appliance(self, height: float) -> None:
    self.current_height += float(height)
    print(f"> Change Height {height}")

  def toggle_electromagnet(self, state: bool) -> None:
    if self.current_eletric_state == False:
      self.current_eletric_state = True
    else:
      self.current_eletric_state = False
    print("> Electromagnet is now: " + str(self.current_eletric_state))

  def get_spear_angle(self) -> float:
    print("Current spear angle: " + str(self.current_degress))
    return self.current_degress
  
  def get_appliance_height(self) -> float:
    print("Current Appliance height: " + str(self.current_height))
    return self.current_height

  def get_electromagnet_state(self) -> bool:
    print("Current eletromagnet state: " + str(self.current_eletric_state))
    return self.current_eletric_state
  
  def get_ultrasonic_distance(self) -> float:
    print("Current ultrasonic distance: " + str(self.current_ultrassonic))
    return self.current_ultrassonic