from configparser import SafeConfigParser

class ConfigurationFile:
    def __init__(self, str_config, modelname):
        config = SafeConfigParser({'N_ITEMS' : '8',                                    
                                   'ESCALA': '5',
                                   'N_OBSERVACIONES': '100'
                                   })
        print(config.read(str_config)  )
               
        print(str_config, config.sections())   
        self.items = config[modelname].getint("ITEMS")
        self.escala = config[modelname].getint("ESCALA")    
        self.observaciones = config[modelname].getint("OBSERVACIONES")        

    def get_items(self):
        return self.items
    
    def get_escala(self):
        return range(self.escala)

    def get_observaciones(self):
        return self.observaciones
