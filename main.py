import datetime

class Saludo():

    # Método mágico para inicializar un objeto
    def __init__(self, nombre):
        self.nombre = nombre
        self.hora = datetime.datetime.now().hour
        self.minutos = datetime.datetime.now().minute
    
    # Método mágico para mostrar los datos de un objeto en String
    def __str__(self):
        return f'Hola {self.nombre} son las {self.hora}:{self.minutos}h'
    
    # Método mágico para sumar dos objetos
    def __add__(self, otro):
        return f'Hola {self.nombre} son las {self.hora}:{self.minutos}h y has recibido {otro.visitas} visitas'

    # Método mágico para destruir un objeto
    def __del__(self):
        print('Objeto destruido')



class Visitas():

    def __init__(self, visitas):
        self.visitas = visitas

saludar = Saludo('Pepito')
visitas = Visitas('1000')

saludo_visitas = saludar + visitas

print(saludo_visitas)