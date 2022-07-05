import paho.mqtt.client as mqtt
from threading import Thread
from datetime import datetime

from integration.ICraneController import ICraneController
from utils.SingletonMetaClass import AbstractSingletonMetaClass
from integration.utils.phy_crane_comm_proto import PhysicalCraneCommunicationProtocol

class WirelessPhysicalCraneController(ICraneController, metaclass=AbstractSingletonMetaClass):
  MQTT_BROKER_HOST = 'localhost'
  MQTT_BROKER_PORT = 1883

  TX_TOPIC = 'crane_controller/channel2'
  TX_QOS = 0

  RX_TOPIC = 'crane_controller/channel1'
  RX_QOS = 0

  def __init__(self):
    self.client = mqtt.Client('paho-mqtt-client')

    self.client.on_connect = self.__on_connect
    self.client.on_disconnect = self.__on_disconnect
    self.client.on_message = self.__on_message

    self.protocol = PhysicalCraneCommunicationProtocol()
    self.crane_state = self.protocol.get_initial_state()

    self.client.connect(self.MQTT_BROKER_HOST, self.MQTT_BROKER_PORT)

    self.client_loop_thread = Thread(target=self.client.loop_forever, kwargs={'timeout': 0.5}, daemon=True)
    self.client_loop_thread.start()

  def reset_crane(self) -> None:
    raise NotImplementedError

  def rotate_spear(self, degrees: int) -> None:
    command = self.protocol.build_rotate_spear_command(degrees)
    self.__send(command)

  def move_appliance(self, height: float) -> None:
    command = self.protocol.build_move_appliance_command(height)
    self.__send(command)

  def toggle_electromagnet(self, state: bool) -> None:
    command = self.protocol.build_toggle_electromagnet_command(state)
    self.__send(command)

  def get_spear_angle(self) -> float:
    return self.crane_state.current_spear_position
  
  def get_appliance_height(self) -> float:
    return self.crane_state.current_appliance_height

  def get_electromagnet_state(self) -> bool:
    return self.crane_state.current_magnet_state
  
  def get_ultrasonic_distance(self) -> float:
    return self.crane_state.measured_distance

  def __on_connect(self, *args, **kwargs) -> None:
    print(f'Connected to {self.MQTT_BROKER_HOST}:{self.MQTT_BROKER_PORT}')
    self.__subscribe_topics()

  def __subscribe_topics(self):
    self.client.subscribe(self.RX_TOPIC, self.RX_QOS)

  def __on_disconnect(self, *args, **kwargs) -> None:
    print(f'Disconnected from {self.MQTT_BROKER_HOST}:{self.MQTT_BROKER_PORT}')
  
  def __on_message(self, client, userdata, msg) -> None:
    now = datetime.now()
    print(f'[{now}] Msg received: {msg.topic} -> {msg.payload}')

    payload = msg.payload.decode('utf-8')

    for data in payload.split(self.protocol.COMM_END):
      if data:
        self.crane_state = self.protocol.process_telemetry(data)

  def __send(self, data: str) -> None:
    self.client.publish(self.TX_TOPIC, data, self.TX_QOS)
