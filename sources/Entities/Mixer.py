from sources.Entities import Block

class Mixer(Block):
    def __init__(self, gain:float, loss:float=0.0, freq_if:float, freq_rf:float):
        super.__init__(self, gain=gain, loss=loss)
        self.gain = gain
        self.loss = loss
        self.Fif = freq_if
        self.Frf = freq_rf