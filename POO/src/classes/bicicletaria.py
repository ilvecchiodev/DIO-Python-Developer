from utils import ClassHelpers

class Bicicleta(ClassHelpers):
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim...')

    def parar(self):
        print('parando....')
        print('parada!')

    def andar(self):
        print('andando...')

    def __str__(self):
       return  super().extract_class_attributes(self) 

