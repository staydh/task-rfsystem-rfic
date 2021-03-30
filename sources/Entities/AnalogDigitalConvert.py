import numpy as np


class AnalogDigitalConvert:
    def __init__(self, minimal_signal_amplitude: float, resistance: float = 50):
        self.minimal_signal_amplitude = minimal_signal_amplitude
        self.resistance = resistance

    @property
    def input_power_in_dbm(self):
        power_in_watt = np.power(self.minimal_signal_amplitude, 2) / self.resistance
        return 10 * np.log10(power_in_watt / 1e-3)
