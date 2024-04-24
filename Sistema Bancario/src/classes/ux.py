
import os
import textwrap

class UX:

    def __init__(self):
      pass
    
    #@staticmethod
    def centralizar_texto(self, texto):
        largura_terminal = os.get_terminal_size().columns
        texto_centralizado = texto.center(largura_terminal)
        return texto_centralizado

    #@staticmethod
    def preencher_linha(self, caractere):
        largura_terminal = os.get_terminal_size().columns
        linha_preenchida = caractere * largura_terminal
        return linha_preenchida
        
    
