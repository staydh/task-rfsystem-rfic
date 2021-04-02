import numpy as np

from .Unit import Unit
from .DBM import DBM
from .Ohm import Ohm


class Volt(Unit):
    def __init__(self, value: float) -> None:
        super().__init__(value=value, unit="V")

    def value_in_dBm(self, resistance: Ohm = Ohm(value=50)) -> DBM:
        value_calculated = 10 * np.log10(
            np.power(self.value, 2) / resistance.value / 1e-3
        )
        power_value = DBM(value=value_calculated)
        return power_value
