from __future__ import annotations

from .Unit import Unit


class DBM(Unit):
    def __init__(self, value: float) -> None:
        super().__init__(value=value, unit="dBm")
