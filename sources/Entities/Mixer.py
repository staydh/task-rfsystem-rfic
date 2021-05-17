from .Block import Block


class Mixer(Block):
    def __init__(
        self,
        gain: float,
        freq_if: float,
        freq_rf: float,
        NF: float,
        loss: float = 0.0,
    ):
        super().__init__(gain=gain, loss=loss, NF=NF)
        self.gain = gain
        self.loss = loss
        self.Fif = freq_if
        self.Frf = freq_rf
