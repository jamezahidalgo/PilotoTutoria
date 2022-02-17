"""
Jazna Meza Hidalgo, 2022

This is a simple and initial version of clustering model
To use main.py, you will require to set the following parameters :
 * -config : A configuration file where a set of parameters for data construction and use is defined.
 * -name: The section name in the configuration file.
 * -mode: [generate, run] for generate or execute of the current model. By default this is set to 'generate'
 * -save: Set true for generate results
"""
import pathlib
import sys
sys.path.append(str(pathlib.Path().absolute()))
from utiles import ConfigurationFile, GenerateData, LoadData, Visualization

import utiles.ConfigurationFile as conf
import utiles.GenerateData as generate
import utiles.LoadData as load
import utiles.Visualization as view

import modelos.KMeans as model

import argparse
import os

if __name__ == '__main__' :        
    parser = argparse.ArgumentParser(description = "Clustering model")
    parser.add_argument("-config", type = str, help = "<str> configuration file", required = True)
    parser.add_argument("-name", type=str, help=" name of section in the configuration file", required = False, default="GENERATE")
    parser.add_argument("-mode", type=str, choices=['generate', 'run'],  help=" generate or run", required = False, default = 'generate')
    parser.add_argument("-save", type= bool,  help=" True to save the file", required = False, default = False)    
    pargs = parser.parse_args()  

    print(pargs.mode, pargs.config)  
    configuration_file = pargs.config 
    configurationFile = conf.ConfigurationFile(pargs.config, pargs.name)   

    print("ITEMS", configurationFile.items)    
    print("OBSERVACIONES", configurationFile.observaciones)       
    print("EXIGENCIA", configurationFile.exigencia)   

    if pargs.mode == 'generate':
        data_generate = generate.Generate(configurationFile,file_output="Simulated_data.csv")
        print("Comenzando a generar los datos en archivo", data_generate.output)
        #data_generate.generate()
        data_generate.calculate_save_from_random()
        print("Datos generados")
        print(data_generate.data_frame)
        visual = view.Visualize(data_generate.data_frame)
        visual.view_histogram(configurationFile.items, "Histograma de puntajes")        
    elif pargs.mode == 'run':
        # Crea el modelo
        print("Creando el modelo ...")
        modelo = model.ModelKMeans("Clustering");
        print("Modelo", modelo.get_name(), "creado ...")
        data_load = load.Load("Simulated_data.csv")
        data_frame = data_load.createDF(sep=",")
        X = data_load.getData()
        print(X)
        # Entrena el modelo
        modelo.fit(X)
        # Predice
        print(modelo.predict(X))    

