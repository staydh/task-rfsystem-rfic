# task-rfsystem

Primeira tarefa da disciplina PSC0043 - Tópicos Especiais em Comunicação I (Circuitos Integrados para Comunicação)

## Definição da tarefa

Elaborar programa para análise em cascata de sistemas de RF: *system budget* e *link budget*

*Guidelines*:

1. Utilizar *python* (.py ou .ipynb), *octave* ou *C/C++*;
2. Utilizar abordagem de modo que o programa possa ser atualizado e interfaceado em tarefas futuras;
3. Definir como entradas, no mínimo: quantidade de sistemas de RF (receptor, transmissor e link); blocos de RF (em cada sistema), ganhos/perdas de cada bloco;
4. Definir como saídas, no mínimo: ganhos de sistema, potência de saída do transmissor, perdas do link, sensibilidade do receptor;
5. Utilizar conversões entre grandezas, caso as entradas não sejam fornecidas em dB ou dBm (V, P e/ou Z, por exemplo);
6. Atualizar descrição do repositório (em ## Início da organização);
7. Manter todo o código em diretório *sources* dentro do repositório;
8. Demonstrar o funcionamento do programa através da resolução do [exercício](ex1.pdf).

## Referências

1. [Ref. 1](https://www.phys.hawaii.edu/~anita/new/papers/militaryHandbook/rcvr_sen.pdf).
2. [RFCafe example](https://www.rfcafe.com/references/electrical/cascade-budget.htm).
3. [Matlab tool example](https://www.mathworks.com/help/rf/ug/superheterodyne-receiver-using-rf-budget-analyzer-app.html)
4. [Python tool example](https://github.com/fronzbot/python-rfdesigner).
5. [ADS example](https://literature.cdn.keysight.com/litweb/pdf/ads2004a/pdf/rfsysbudget.pdf).

## Prazos máximos

- Commit de versão inicial: 29/03 (*sources* e descrição inicial)
- Commit de versão intermediária: 31/03 (*sources*, descrição incluíndo a demonstração)
- Prazo para issues/pull requests: 02/04
- Commit de versão final: 05/04 (*sources* finais e descrição completa)
## Inicio da organização

### RF Analyzer

This project is about a python radio frequency budget analysis package.


#### Architecture

In general the package is organized by entities and services. Each entity represents a block of a radio frequency system (Antenna, Amplifier, ...). Each service is a class with its especific static execute method that make operations related with an entity like calculate gain of a system, link losses and so on.


#### Usage

You should instantiate a system and provide a list of blocks to it. With a system, you can use the services class to do budget analysis.

### Behavior
This project 

### Variables


### Entities

### Service
The services folder should be used for entities methods purposes (accordingly to S.O.L.I.D. principles).

### Units
The units should be used as a entity parameter for physical quantities. Each entity will have your  unity inside your own constructor.

Units implemented:

* Ampere;
* dBm;
* Ohm;
* Unit (Parent);
* Volt;
* Watt.

### Example

The test.py file in the root of this repository has a implemmentation example.

```py
[9:03 PM, 4/1/2021] +55 84 9950-4859: ```python
[9:03 PM, 4/1/2021] +55 84 9950-4859: distance = 70e3 # m
frequency = 95.7e6 # Hz

link = Link(distance=distance, frequency=frequency)
propagation_losses = GetLinkLossService.execute(link=link)
print(f"Propagation Loss: {propagation_losses} dBm")
''' 
