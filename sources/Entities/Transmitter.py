import numpy as np


class Transmitter:
    # output_power in watts
    def __init__(self, output_power: float) -> None:
        self.output_power = output_power

    @property
    def power_in_dBm(self) -> float:
        return 10 * np.log(self.output_power / 1e-3)
