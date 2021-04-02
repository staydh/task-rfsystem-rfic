from __future__ import annotations
from ..Errors.UnitOperationError import UnitOperationError


class Unit:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}{self.unit}"

    def __add__(self, value: Unit) -> Unit:
        type_of_value_to_add = type(value)
        can_calculate = isinstance(self, type_of_value_to_add)
        if not can_calculate:
            raise UnitOperationError()
        calculated_value = self.value + value.value
        calculated_unit = Unit(value=calculated_value, unit=self.unit)
        return calculated_unit
