import numpy as np


class Block:
    def __init__(self, gain: float, loss: float):
        self.gain = gain
        self.loss = loss

    @property
    def gain_in_dbm(self):
        return 10 * np.log(self.gain / 1e-3)
