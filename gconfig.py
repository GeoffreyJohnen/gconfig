import configparser
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GConfigWindow(QMainWindow):

  def __init__(self, *args, **kwargs):
    super(GConfigWindow, self).__init__(*args, **kwargs)

    self.gconfig = configparser.ConfigParser()
    self.gconfig.optionxform = str #Make the configParser case sensistive
    self.gconfig.read('gconfig.ini')

    self.sections = self.gconfig.sections()
    self.gconfig_dict = {} #Store a dictionnary with sections as key and values in list
    self.bool_possible_list = ['true','false','True','False']

    self.app = QApplication(sys.argv)
    self.setWindowTitle('GConfig')
    layout = QFormLayout()
    for section in self.sections:
      self.gconfig_dict[section]=[]
      for key in self.gconfig[section]:
        self.gconfig_dict[section].append(key)
        print(key)
        if self._is_bool(section,key):
          bool_widget = QComboBox()
          bool_widget.addItems(['True','False'])
          layout.addRow(key,bool_widget)
        layout.addRow(key,QLineEdit())
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

  def _is_bool(self,section,key):
    is_bool = False
    if self.gconfig[section][key] in self.bool_possible_list:
      is_bool = True
    return is_bool


#Opening the config file
#----------------------------------------------

#----------------------------------------------

#Analyse the config file and get the structure 
#into config_dict
#----------------------------------------------

app = QApplication(sys.argv)
window = GConfigWindow()
window.show()
#layout.addRow('Time',QDateTimeEdit())
#window.setLayout(layout)
#window.show()
sys.exit(app.exec_())


