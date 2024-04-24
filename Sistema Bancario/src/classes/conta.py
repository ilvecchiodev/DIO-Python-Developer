from datetime import datetime
import random

class Conta():

    cpf = None
    numero_conta = None
    agencia = None
    data_criacao = None

    def __init__(self, cpf):
        self.cpf = cpf
        self.data_criacao = datetime.now().strftime('%d/%m/%Y')
        self.numero_conta = self._gerar_numero_conta()
        self.agencia= "0001"

    def _gerar_numero_conta(self):
        return random.randint(100000, 999999)

    def __getitem__(self, key): 
        return self.cpf == key
    
    def __repr__(self):
        return repr([self.cpf, self.data_criacao, self.numero_conta, self.agencia])
        