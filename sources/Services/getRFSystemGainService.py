from ..Entities.RFSystem import RFSystem


class getRFSystemGainService:
    @staticmethod
    def execute(rf_system: RFSystem) -> float:
        blocks = rf_system.blocks
        systemGain = sum([block.gain for block in blocks])
        return systemGain
