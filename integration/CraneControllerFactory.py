from distutils.command.config import config
from enum import Enum

from integration.ICraneController import ICraneController
from integration.PhysicalCraneController import PhysicalCraneController
from integration.WirelessPhysicalCraneController import WirelessPhysicalCraneController
from integration.SimulatedCraneController import SimulatedCraneController
from integration.temp_ICraneController import TempICraneController
from utils.Config import Config

class Variant(Enum):
  Physical = 'physical'
  Simulated = 'simulated'
  Temporary = 'temporary'

class CraneControllerFactory:
  @classmethod
  def create(cls, variant: Variant) -> ICraneController:
    config = Config()

    if variant == Variant.Physical:
      if config.get_config('UsingWireless'):
        return WirelessPhysicalCraneController()
      else:
        return PhysicalCraneController()
    
    if variant == Variant.Simulated:
      return SimulatedCraneController()
    
    if variant == Variant.Temporary:
      return TempICraneController()
    
    raise ValueError(f'Unknown variant: {variant}')