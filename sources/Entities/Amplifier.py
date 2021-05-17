from sources.Entities.Block import Block


class Amplifier(Block):
    def __init__(self, gain: float, loss: float, NF):
        super().__init__(gain=gain, loss=loss, NF=NF)
