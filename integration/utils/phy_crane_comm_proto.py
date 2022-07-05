class CraneState:
  def __init__(self):
    self.current_spear_position = 0
    self.current_appliance_height = 0
    self.current_magnet_state = 0
    self.measured_distance = 0

class PhysicalCraneCommunicationProtocol:
  COMM_SEP = ':'
  COMM_END = '\n'

  @staticmethod
  def get_initial_state() -> CraneState:
    return CraneState()

  @classmethod
  def process_telemetry(cls, data: str) -> CraneState:
    values = data.split(cls.COMM_SEP)
    
    state = CraneState()

    state.current_spear_position = float(values[0])
    state.current_appliance_height = float(values[1])
    state.current_magnet_state = bool(values[2])
    state.measured_distance = float(values[3])

    return state
  
  @classmethod
  def build_rotate_spear_command(cls, degrees: int) -> str:
    return f'spear:set:{degrees}' + cls.COMM_END

  @classmethod
  def build_move_appliance_command(cls, height: float) -> str:
    return f'appliance:set:{height}' + cls.COMM_END

  @classmethod
  def build_toggle_electromagnet_command(cls, state: bool) -> str:
    return f'magnet:set:{int(state)}' + cls.COMM_END