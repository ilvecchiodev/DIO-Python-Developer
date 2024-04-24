
class Bicicleta():
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
      props = '\n'.join([f'{key}: {value}' for key, value in self.__dict__.items()])
      return f'{self.__class__}\n{props}'
    