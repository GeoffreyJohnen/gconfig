import configparser
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('GConfig')
layout = QFormLayout()


sections = config.sections()
number_of_sections = len(sections)
config_dict = {}
for section in sections:
  config_dict[section]=[]
  for key in config[section]:
    config_dict[section].append(key)
    if is_bool(section,key):
      bool_widget = QComboBox()
      bool_widget.addItems(['True','False'])
      layout.addRow(key,bool_widget)
    layout.addRow(key,QLineEdit())
layout.addRow('Time',QDateTimeEdit())
window.setLayout(layout)
window.show()
sys.exit(app.exec_())


