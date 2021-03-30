from sources.Entities.Amplifier import Amplifier
from sources.Entities.Antenna import Antenna
from sources.Entities.Link import Link
from sources.Services.GetLinkLossService import GetLinkLossService

distance = 70e3  # m
frequency = 95.7e6  # Hz

# Part 1
link = Link(distance=distance, frequency=frequency)
propagation_losses = GetLinkLossService.execute(link=link)
print(propagation_losses)

# Part 2
transmitter_antenna_gain = 20
transmitter_antenna = Antenna(gain=transmitter_antenna_gain)
amplifier = Amplifier(gain=10e3, loss=0)
transmitted_output_power = (
    transmitter_antenna.gain_in_dbm + amplifier.gain_in_dbm - propagation_losses
)

# Part 3
