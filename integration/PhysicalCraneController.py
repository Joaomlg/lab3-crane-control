from serial import Serial
from threading import Thread, Lock
from time import sleep

from integration.ICraneController import ICraneController
from utils.SingletonMetaClass import AbstractSingletonMetaClass

class PhysicalCraneController(ICraneController, metaclass=AbstractSingletonMetaClass):
  COMM_SEP = ':'

  def __init__(self, port: str = 'COM4'):
    self.serial = Serial(port)
    self.serial_lock = Lock()

    self.current_spear_position = 0
    self.current_appliance_height = 0
    self.current_magnet_state = 0
    self.measured_distance = 0

    self.process_telemetry_thread = Thread(target=self.process_telemetry, daemon=True)
    self.process_telemetry_thread.start()
  
  def process_telemetry(self) -> None:
    while True:
      recv = self.__read_serial_threadsafe()

      if recv:
        values = recv.split(self.COMM_SEP)

        self.current_spear_position = float(values[0])
        self.current_appliance_height = float(values[1])
        self.current_magnet_state = bool(values[2])
        self.measured_distance = float(values[3])

      sleep(0.1)

  def reset_crane(self) -> None:
    raise NotImplementedError

  def rotate_spear(self, degrees: int) -> None:
    self.__write_serial_threadsafe(f'spear:set:{degrees}')

  def move_appliance(self, height: float) -> None:
    self.__write_serial_threadsafe(f'spear:set:{height}')

  def toggle_electromagnet(self, state: bool) -> None:
    self.__write_serial_threadsafe(f'spear:set:{int(state)}')

  def get_spear_angle(self) -> float:
    return self.current_spear_position
  
  def get_appliance_height(self) -> float:
    return self.current_appliance_height

  def get_electromagnet_state(self) -> bool:
    return self.current_magnet_state
  
  def get_ultrasonic_distance(self) -> float:
    return self.measured_distance

  def __write_serial_threadsafe(self, data: str) -> None:
    with self.serial_lock:
      if not data.endswith('\n'):
        data += '\n'
      self.serial.write(data.encode('utf-8'))
  
  def __read_serial_threadsafe(self) -> None:
    with self.serial_lock:
      if self.serial.in_waiting:
        recv = self.serial.readline()
        return recv.decode('utf-8')
