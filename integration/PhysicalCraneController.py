from serial import Serial
from threading import Thread, Lock
from time import sleep

from integration.ICraneController import ICraneController
from integration.utils.phy_crane_comm_proto import PhysicalCraneCommunicationProtocol
from utils.SingletonMetaClass import AbstractSingletonMetaClass

class PhysicalCraneController(ICraneController, metaclass=AbstractSingletonMetaClass):
  def __init__(self, port: str = 'COM4'):
    self.serial = Serial(port)
    self.serial_lock = Lock()

    self.protocol = PhysicalCraneCommunicationProtocol()

    self.crane_state = self.protocol.get_initial_state()

    self.recv_thread = Thread(target=self.recv_thread_routine, daemon=True)
    self.recv_thread.start()
  
  def recv_thread_routine(self) -> None:
    while True:
      recv = self.__read_serial_threadsafe()

      if recv:
        self.crane_state = self.protocol.process_telemetry(recv)

      sleep(0.1)

  def reset_crane(self) -> None:
    raise NotImplementedError

  def rotate_spear(self, degrees: int) -> None:
    command = self.protocol.build_rotate_spear_command(degrees)
    self.__write_serial_threadsafe(command)

  def move_appliance(self, height: float) -> None:
    command = self.protocol.build_move_appliance_command(height)
    self.__write_serial_threadsafe(command)

  def toggle_electromagnet(self, state: bool) -> None:
    command = self.protocol.build_toggle_electromagnet_command(state)
    self.__write_serial_threadsafe(command)

  def get_spear_angle(self) -> float:
    return self.crane_state.current_spear_position
  
  def get_appliance_height(self) -> float:
    return self.crane_state.current_appliance_height

  def get_electromagnet_state(self) -> bool:
    return self.crane_state.current_magnet_state
  
  def get_ultrasonic_distance(self) -> float:
    return self.crane_state.measured_distance

  def __write_serial_threadsafe(self, data: str) -> None:
    with self.serial_lock:
      self.serial.write(data.encode('utf-8'))
  
  def __read_serial_threadsafe(self) -> None:
    with self.serial_lock:
      if self.serial.in_waiting:
        recv = self.serial.readline()
        return recv.decode('utf-8')
