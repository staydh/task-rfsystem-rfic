"""
Classe implementada para descrição do sistema de Transmissão;
Na classe são descritos os atributos de um transmissor de RF

"""
from .RFSystem import RFSystem
from typing import List
import numpy as np


class Transmitter(RFSystem):
    # output_power in watts
    def __init__(self, blocks: List, output_power: float) -> None:
        super().__init__(blocks=blocks)
        self.output_power = output_power
        self.blocks = blocks

    @property
    def power_in_dBm(self) -> float:
        return 10 * np.log(self.output_power / 1e-3)
