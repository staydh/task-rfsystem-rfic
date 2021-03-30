from typing import List
from .Block import Block


class RFSystem:
    def __init__(self, blocks: List[Block]):
        self.blocks = blocks
