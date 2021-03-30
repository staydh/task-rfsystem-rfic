import numpy as np


class DigitalAnalogConverter:
    def __init__(self, signal_amplitude: float, resistance: float):
        self.signal_amplitude = signal_amplitude
        self.resistance = resistance

    @property
    def out_power_in_dbm(self):
        power_in_watt = np.power(self.signal_amplitude, 2) / self.resistance
        return 10 * np.log10(power_in_watt / 1e-3)
