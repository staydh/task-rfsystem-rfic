from sources.Entities.Block import Block


class Antenna(Block):
    def __init__(self, gain: float, NF: float, loss: float = 0) -> None:
        super().__init__(gain=gain, loss=loss, NF=NF)
