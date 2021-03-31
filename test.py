from sources.Entities.Amplifier import Amplifier
from sources.Entities.Antenna import Antenna
from sources.Entities.Link import Link
from sources.Entities.Mixer import Mixer
from sources.Entities.Filter import Filter
from sources.Services.GetLinkLossService import GetLinkLossService
from sources.Units.Volt import Volt
from sources.Units.Watt import Watt

distance = 70e3  # m
frequency = 95.7e6  # Hz

# Part 1
link = Link(distance=distance, frequency=frequency)
propagation_losses = GetLinkLossService.execute(link=link)
print(propagation_losses)
print(f"Propagation Loss: {propagation_losses} dBm")

# Part 2
transmitter_antenna_gain = 20
transmitter_antenna = Antenna(gain=transmitter_antenna_gain)
transmitter_amplifier = Amplifier(gain=10e3, loss=0)
receiver_sensitivity = (
    transmitter_antenna.gain_in_dbm
    + transmitter_amplifier.gain_in_dbm
    - propagation_losses
)
print(f"Amplifier power {transmitter_amplifier.gain_in_dbm}")
print(f"RX input sensitivity: {receiver_sensitivity}")
# Part 3
input_tx_voltage = Volt(value=20)
input_tx_voltage_in_dBm = input_tx_voltage.value_in_dBm()
print(f"TX input is {input_tx_voltage_in_dBm}")
output_tx_power = Watt(value=10e3)
output_tx_power_in_dBm = output_tx_power.value_in_dBm()
print(f"TX output is {output_tx_power_in_dBm}")

first_amplifier = Amplifier(gain=21, loss=0)
mixer = Mixer(gain=0, loss=15, freq_if=455e3, freq_rf=95.7e6)
filter_component = Filter(gain=0, loss=1)
second_amplifier = Amplifier(gain=21, loss=0)

output_rx_voltage = Volt(value=50e-3)
output_rx_in_dBm = output_rx_voltage.value_in_dBm()
print(f"Output from RX is {output_rx_in_dBm}")


# Amplifier

# amplifier = Amplifier(gain)
