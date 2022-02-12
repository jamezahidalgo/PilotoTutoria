import numpy as np

class Generate:
    def __init__(self, file_output="Generate.csv", header = "RUT", items = 8, 
            escala = 5, observaciones = 150) :
        self.output = file_output
        self.header = header
        self.items = items
        self.escala = range(1,escala+1)
        self.observaciones = observaciones

    def generate(self):
        archivo = open(self.output,"w")

        for item in range(1, self.items+1):
            self.header = self.header + ";I" + str(item);
        archivo.write(self.header + "\n")

        for index in range(1, self.observaciones+1):
            line = str(index)
            for item in range(1, self.items+1):
                logro = np.random.randint(5)
                line = line + ";" + str(self.escala[logro])
        
            archivo.write(line + "\n")
        archivo.close()

    def get_output(self):
        return self.output
    