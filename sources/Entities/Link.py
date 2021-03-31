"""
Classe para descrição do sistema Link (Espaço livre entre as antenas de
transmissão e recepção);
Na classe são declarados os principais atributos do Link.

"""
from .RFSystem import RFSystem
from typing import List


class Link(RFSystem):
    def __init__(self, distance: float, frequency: float):
        super().__init__(blocks=[])
        self.distance = distance
        self.frequency = frequency
