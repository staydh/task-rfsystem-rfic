import numpy as np


class Block:
    def __init__(self, gain: float, loss: float, NF: float):
        self.gain = gain
        self.loss = loss
        self.noise_figure = NF

    @property
    def gain_in_dbm(self):
        return 10 * np.log10(self.gain / 1e-3)

    @property
    def noise_figure_in_watt(self):
        return 10 ** (self.noise_figure / 10)
