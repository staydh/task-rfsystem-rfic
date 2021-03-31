import numpy as np

from .Unit import Unit
from .DBM import DBM


class Watt(Unit):
    def __init__(self, value: float) -> None:
        super().__init__(value=value, unit="W")

    def value_in_dBm(self) -> DBM:
        value_calculated = 10 * np.log10(self.value / 1e-3)
        power_value = DBM(value=value_calculated)
        return power_value
