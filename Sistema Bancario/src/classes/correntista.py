from classes.conta import Conta
from classes.usuario import Usuario

class Correntista(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf, 'correntista')
        self.conta = []
    
    def __getitem__(self, key): 
       return self.cpf == key
    
    def __repr__(self):
        return repr([self.nome, self.cpf, self.conta])
