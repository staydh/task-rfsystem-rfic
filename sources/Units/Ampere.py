from .Unit import Unit
from .Volt import Volt
from .Watt import Watt


class Ampere(Unit):
    def __init__(self, value):
        super().__init__(self, value=value, unit="A")
