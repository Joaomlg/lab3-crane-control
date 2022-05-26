import math
from integration.ICraneController import ICraneController
from utils.SingletonMetaClass import AbstractSingletonMetaClass
import zmqRemoteApi
import math
import time

VELOCITY_SPEAR = .25
VELOCITY_APPLIANCE = .15

class SimulatedCraneController(ICraneController, metaclass=AbstractSingletonMetaClass):
  def __init__(self):
    try : 
      self.sim = zmqRemoteApi.RemoteAPIClient().getObject('sim')
      print("Connected to simulation")
    except :
      print("Could not connect to the simulation.")
      exit()
    self.spear = self.sim.getObject('/Arm_actuator')
    self.app = self.sim.getObject('/Hoist_actuator')
    
    self.sim.startSimulation()
    self.spear_angle = .0
    self.appliance_height = .0

  def reset_crane(self) -> None:
    self.sim.stopSimulation()
    self.sim.startSimulation()
    self.spear_angle = .0
    self.appliance_height = .0

  def rotate_spear(self, degrees: float) -> None:
    multiplier = 1
    if degrees < 0:
      multiplier = -1

    sleep_time = degrees/(VELOCITY_SPEAR * (180/math.pi))
    self.sim.setJointTargetVelocity(self.spear, multiplier * VELOCITY_SPEAR)
    time.sleep(sleep_time)
    self.sim.setJointTargetVelocity(self.spear, 0)
    
    self.spear_angle += degrees

  def move_appliance(self, height: float) -> None:
    # TODO: Calc appliance limits and filter
    multiplier = 1
    if height < 0:
      multiplier = -1

    sleep_time = height * VELOCITY_APPLIANCE
    self.sim.setJointTargetVelocity(self.spear, multiplier * VELOCITY_APPLIANCE)
    time.sleep(sleep_time)
    self.sim.setJointTargetVelocity(self.spear, 0)

    self.height += height

  def toggle_electromagnet(self, state: bool) -> None:
    raise NotImplementedError

  def get_spear_angle(self) -> float:
    return self.spear_angle
  
  def get_appliance_height(self) -> float:
    return self.appliance_height

  def get_electromagnet_state(self) -> bool:
    raise NotImplementedError
  
  def get_ultrasonic_distance(self) -> float:
    raise NotImplementedError