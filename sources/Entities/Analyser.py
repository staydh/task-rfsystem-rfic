from typing import List
from .RFSystem import RFSystem


class Analyzer:
    def __init__(self, rf_systems: List[RFSystem]):
        self.rf_systems = rf_systems
