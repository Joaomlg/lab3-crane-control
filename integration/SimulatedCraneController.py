import math
# from integration.ICraneController import ICraneController
from ICraneController import ICraneController # TO remove
import zmqRemoteApi as zmqRemoteApi # TO remove
import time

VELOCITY_SPEAR = .25
VELOCITY_APPLIANCE = .015
SIMULATION_DISTANCE = 42
REAL_DISTANCE = 27

class SimulatedCraneController(ICraneController):
  def __init__(self):
    try : 
      # import integration.zmqRemoteApi as zmqRemoteApi
      self.sim = zmqRemoteApi.RemoteAPIClient().getObject('sim')
      print("Connected to simulation")
    except :
      print("Could not connect to the simulation.")
      exit()
    self.spear = self.sim.getObject('/armActuator')
    self.app = self.sim.getObject('/hoistActuator')
    self.sensor = self.sim.getObject("/distanceSensor")
    
    self.sim.startSimulation()
    self.spear_angle = .0
    self.appliance_height = .0

  def reset_crane(self) -> None:
    self.sim.stopSimulation()
    self.sim.startSimulation()
    self.spear_angle = .0
    self.appliance_height = .0
    self.eletromagnatic_state = False

  def rotate_spear(self, degrees: float) -> None:
    multiplier = 1
    if degrees < 0:
      multiplier = -1

    radians = degrees/180 * math.pi
    position = self.sim.getJointPosition(self.spear)
    target_radians = position + radians
    self.sim.setJointTargetVelocity(self.spear, multiplier * VELOCITY_SPEAR)
    
    while True:
      position = self.sim.getJointPosition(self.spear)
      if (multiplier == 1 and position > target_radians) or (multiplier == -1 and position < target_radians):
        break

    self.sim.setJointTargetVelocity(self.spear, 0)

  def move_appliance(self, height: float) -> None:
    multiplier = 0
    height = height/100 * SIMULATION_DISTANCE/REAL_DISTANCE
    position = -1 * self.sim.getJointPosition(self.app)
    target_position = position + height*-1
    if height > 0:
      multiplier = 1
    else:
      multiplier = -1

    self.sim.setJointTargetVelocity(self.app, multiplier * VELOCITY_APPLIANCE)

    while True:
      position = -1 * self.sim.getJointPosition(self.app)
      if (multiplier == -1 and position > target_position) or (multiplier == 1 and position < target_position):
        break

    self.sim.setJointTargetVelocity(self.app, 0)

    position = -1 * self.sim.getJointPosition(self.app)

    self.appliance_height = position * 100 * REAL_DISTANCE/SIMULATION_DISTANCE

  def toggle_electromagnet(self, state: bool) -> None:
    self.eletromagnatic_state = state
    self.sim.pushUserEvent("toggleEletromagnet", -1, -1, {"state": state})

  def get_spear_angle(self) -> float:
    return self.spear_angle
  
  def get_appliance_height(self) -> float:
    return self.appliance_height

  def get_electromagnet_state(self) -> bool:
    return self.eletromagnatic_state
  
  def get_ultrasonic_distance(self) -> float:
    data = self.sim.readProximitySensor(self.sensor)
    return data[1]

if __name__ == "__main__":
  pass
  # simulatedCrane = SimulatedCraneController()
  # Active eletromagnetic
  # time.sleep(1)
  # simulatedCrane.toggle_electromagnet(True)
  # time.sleep(1)
  # simulatedCrane.toggle_electromagnet(False)
  # time.sleep(1)
  # simulatedCrane.toggle_electromagnet(True)

  # Move Applience
  # simulatedCrane.move_appliance(-10)
  # time.sleep(1)
  # simulatedCrane.move_appliance(5)
  # time.sleep(1)
  # simulatedCrane.move_appliance(-20)

  # Rotate Spear
  # simulatedCrane.rotate_spear(90)
  # time.sleep(1)
  # simulatedCrane.rotate_spear(-45)
  # time.sleep(1)
  # simulatedCrane.rotate_spear(20)
  # time.sleep(1)
  # simulatedCrane.rotate_spear(270)

  # simulatedCrane.toggle_electromagnet(True)
  # simulatedCrane.move_appliance(-23.2)
  # time.sleep(1)
  # simulatedCrane.move_appliance(23)
  # simulatedCrane.rotate_spear(90)
  # simulatedCrane.toggle_electromagnet(False)


