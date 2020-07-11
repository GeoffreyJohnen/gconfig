import configparser

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



