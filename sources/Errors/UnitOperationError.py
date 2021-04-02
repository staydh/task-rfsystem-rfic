class UnitOperationError(Exception):
    """Raise when an unit is trying to add or subtract by a different type unit"""

    def __init__(
        self,
        message: str = "Operation not allowed for different unit types",
    ) -> None:
        super().__init__(message)
