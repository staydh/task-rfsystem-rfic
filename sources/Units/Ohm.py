from .Unit import Unit


class Ohm(Unit):
    def __init__(self, value):
        super().__init__(value=value, unit="R")
