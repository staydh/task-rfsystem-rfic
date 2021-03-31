'''
Classe implementada para descrição do sistema de Recepção;
Na classe são descritos os atributos de um receptor de RF
'''


from Entities import RFSystem
from typing import List

class Receiver(RFSystem):
    def __init__(self, blocks:List, pin:float) -> None:
        super.__init__(self, blocks = blocks )
        self.blocks = blocks
        self.sensitivity = pin 
