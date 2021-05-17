from ..Entities.RFSystem import RFSystem


class GetSystemNoiseFigureService:
    @staticmethod
    def execute(rfSystem: RFSystem) -> float:
        noise_figure = 0.0
        for (index, block) in enumerate(rfSystem.blocks):
            if index == 0:
                noise_figure += block.noise_figure_in_watt
            else:
                numerator = block.noise_figure_in_watt - 1
                divider = 1.0
                for i in range(1, index + 1):
                    divider *= rfSystem.blocks[i - 1].gain
                noise_figure += numerator / divider
        return noise_figure
