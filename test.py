from sources.Units.DBM import DBM
from sources.Entities.Amplifier import Amplifier
from sources.Entities.Antenna import Antenna
from sources.Entities.Link import Link
from sources.Entities.Mixer import Mixer
from sources.Entities.Filter import Filter
from sources.Entities.Transmitter import Transmitter
from sources.Entities.Receiver import Receiver
from sources.Services.GetLinkLossService import GetLinkLossService
from sources.Units.Volt import Volt
from sources.Units.Watt import Watt

distance = 70e3  # m
frequency = 95.7e6  # Hz

# Part 1
link = Link(distance=distance, frequency=frequency)
propagation_losses = GetLinkLossService.execute(link=link)
print(f"Propagation Loss: {propagation_losses} dBm")

# Part 2
transmitter_antenna_gain = 20
transmitter_antenna = Antenna(gain=transmitter_antenna_gain)
transmitter_amplfier_gain = Watt(10e3)
transmitter_output_gain_in_dBm = transmitter_amplfier_gain.value_in_dBm()
transmitter_amplifier_output = Amplifier(
    gain=transmitter_output_gain_in_dBm.value, loss=0
)

receiver_antenna_gain = DBM(value=20)

receiver_sensitivity = (
    transmitter_antenna.gain
    + transmitter_amplifier_output.gain
    - propagation_losses
    + receiver_antenna_gain.value
)


# Part 3
input_tx_voltage = Volt(value=20)
input_tx_voltage_in_dBm = input_tx_voltage.value_in_dBm()
output_tx_power = Watt(value=10e3)
output_tx_power_in_dBm = output_tx_power.value_in_dBm()

transmitter = Transmitter(
    blocks=[
        Amplifier(gain=21, loss=0),
        Mixer(gain=0, loss=10, freq_if=455e3, freq_rf=95.7e6),
        Filter(gain=0, loss=1),
        Amplifier(gain=21, loss=0),
    ],
    output_power=output_tx_power_in_dBm.value,
)

receiver = Receiver(
    blocks=[
        Filter(gain=0, loss=1),
        Amplifier(gain=5, loss=0),
        Filter(gain=0, loss=1),
        Mixer(gain=-10, loss=10, freq_if=10.7e6, freq_rf=95.7e6),
        Filter(gain=0, loss=1),
        Mixer(gain=-10, loss=10, freq_if=455e3, freq_rf=10.7e6),
        Filter(gain=0, loss=1),
        Amplifier(gain=5, loss=0),
    ],
    pin=receiver_sensitivity,
)

output_rx_voltage = Volt(value=50e-3)
output_rx_in_dBm = output_rx_voltage.value_in_dBm()

# Parte 4

print("\nDados do transmissor")
print(f"Entrada: {input_tx_voltage_in_dBm.value:.3f}dBm")
for index, block in enumerate(transmitter.blocks):
    print(f"bloco {index} ({type(block).__name__}): {block.gain-block.loss}dBm")
print(f"Saída: {output_tx_power_in_dBm}")

print("\nDados do receptor")
print(f"Entrada: {receiver_sensitivity:.3f}dBm")
for index, block in enumerate(receiver.blocks):
    print(f"block {index} ({type(block).__name__}): {block.gain-block.loss}dBm")
print(f"Saída: {output_rx_in_dBm.value:.3f}dBm")
