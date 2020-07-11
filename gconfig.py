import configparser
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
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
    layout.addRow(key,QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec_())


