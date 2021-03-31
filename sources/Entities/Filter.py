from .Block import Block


class Filter(Block):
    def __init__(self, gain: float = 0.0, loss: float = 0.0):
        super().__init__(gain=gain, loss=loss)
        self.gain = gain
        self.loss = loss
