import configparser
import os
from typing import Any

from utils.SingletonMetaClass import SingletonMetaClass

class Config(metaclass=SingletonMetaClass):
  filename = 'config.ini'

  def __init__(self, dir=None):
    if not dir:
      dir = os.path.curdir

    full_filename = os.path.realpath(os.path.join(dir, self.filename))

    self.configs = configparser.ConfigParser()
    self.configs.read(full_filename)

  def get_config(self, key:str, env:str='Default') -> Any:
    return self.configs.get(env, key)