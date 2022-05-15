from enum import Enum

from integration.ICraneController import ICraneController
from integration.PhysicalCraneController import PhysicalCraneController
from integration.SimulatedCraneController import SimulatedCraneController

class Variant(Enum):
  Physical = 'physical'
  Simulated = 'simulated'

class CraneControllerFactory:
  @classmethod
  def create(variant: Variant) -> ICraneController:
    if variant == Variant.Physical:
      return PhysicalCraneController()
    
    if variant == Variant.Simulated:
      return SimulatedCraneController()
    
    raise ValueError(f'Unknown variant: {variant}')