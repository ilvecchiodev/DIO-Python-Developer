

from datetime import datetime


class Transacao:

    def __init__(self, numero_conta, tipo, valor, data_hora):
        self.numero_conta = numero_conta
        self.tipo = tipo
        self.valor = valor
        self.data = data_hora


 