import math
from integration.ICraneController import ICraneController
import integration.zmqRemoteApi as zmqRemoteApi
# from ICraneController import ICraneController # TO remove
# import zmqRemoteApi as zmqRemoteApi # TO remove
import time

VELOCITY_SPEAR = .05
VELOCITY_APPLIANCE = .015
SIMULATION_DISTANCE = 43
REAL_DISTANCE = 27

class SimulatedCraneController(ICraneController):
  def __init__(self):
    try : 
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
    time.sleep(2)
    self.sim.startSimulation()
    self.spear_angle = .0
    self.appliance_height = .0
    self.eletromagnatic_state = False

  def rotate_spear(self, degrees: float) -> None:
    # TODO: fix problem to ratate mora than 360º
    degrees = float(degrees)
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
    position = self.sim.getJointPosition(self.spear)
    self.spear_angle = position*180/math.pi


  def move_appliance(self, height: float) -> None:
    multiplier = 0
    height = float(height)
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
      if (multiplier == -1 and (position > target_position or position > SIMULATION_DISTANCE/100)) or (multiplier == 1 and position < target_position or position <= 0):
        break

    self.sim.setJointTargetVelocity(self.app, 0)

    position = -1 * self.sim.getJointPosition(self.app)

    self.appliance_height = position * 100 * REAL_DISTANCE/SIMULATION_DISTANCE

  def toggle_electromagnet(self, state: bool) -> None:
    self.eletromagnatic_state = state
    message = state == 1
    self.sim.pushUserEvent("toggleEletromagnet", -1, -1, {"state": message})

  def get_spear_angle(self) -> float:
    return self.spear_angle
  
  def get_appliance_height(self) -> float:
    return self.appliance_height

  def get_electromagnet_state(self) -> bool:
    return self.eletromagnatic_state
  
  def get_ultrasonic_distance(self) -> float:
    data = self.sim.readProximitySensor(self.sensor)
    return data[1] * 100 * REAL_DISTANCE/SIMULATION_DISTANCE

if __name__ == "__main__":
  pass
  simulatedCrane = SimulatedCraneController()
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

  # Challenger
  # simulatedCrane.toggle_electromagnet(True)
  # simulatedCrane.move_appliance(-26.61)
  # time.sleep(1)
  # simulatedCrane.move_appliance(26.61)
  # simulatedCrane.rotate_spear(90)
  # simulatedCrane.toggle_electromagnet(False)


