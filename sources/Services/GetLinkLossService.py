import numpy as np
from ..Entities.Link import Link


class GetLinkLossService:
    @staticmethod
    def execute(link: Link) -> float:
        L_FS = 20 * np.log10(link.distance) + 20 * np.log10(link.frequency) - 147.55
        return L_FS
