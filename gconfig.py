import configparser
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def is_bool(section,key):
  is_bool = False
  bool_list = ['true','false','True','False']
  if config[section][key] in bool_list:
    is_bool = True
  return is_bool

#Opening the config file
#----------------------------------------------
config = configparser.ConfigParser()
config.read('config.ini')
#----------------------------------------------

#Analyse the config file and get the structure 
#into config_dict
#----------------------------------------------
sections = config.sections()
number_of_sections = len(sections)
config_dict = {}
for section in sections:
  config_dict[section]=[]
  for key in config[section]:
    config_dict[section].append(key)
    print(is_bool(section,key))




