from enum import Enum

from integration.ICraneController import ICraneController
from integration.PhysicalCraneController import PhysicalCraneController
from integration.SimulatedCraneController import SimulatedCraneController
from integration.temp_ICraneController import TempICraneController

class Variant(Enum):
  Physical = 'physical'
  Simulated = 'simulated'
  Temporary = 'temporary'

class CraneControllerFactory:
  @staticmethod
  def create(variant: Variant) -> ICraneController:
    if variant == Variant.Physical:
      return PhysicalCraneController()
    
    if variant == Variant.Simulated:
      return SimulatedCraneController()
    
    if variant == Variant.Temporary:
      return TempICraneController()
    
    raise ValueError(f'Unknown variant: {variant}')