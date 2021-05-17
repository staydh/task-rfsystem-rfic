from sources.Services.GetSystemNoiseFigureService import GetSystemNoiseFigureService
from sources.Entities.Receiver import Receiver
from sources.Entities.Amplifier import Amplifier
from sources.Entities.Mixer import Mixer
from sources.Entities.Filter import Filter

receiver = Receiver(
    blocks=[
        Filter(gain=0.891, loss=0, NF=0.5),
        Amplifier(gain=100, loss=0, NF=3),
        Filter(gain=0.794, loss=0, NF=1),
        Mixer(gain=0.251, loss=0, freq_if=455e3, freq_rf=95.7e6, NF=6),
        Amplifier(gain=1000, loss=0, NF=5),
    ],
    pin=10,
)

system_noise = GetSystemNoiseFigureService.execute(rfSystem=receiver)
print(f"{system_noise:.04}")
