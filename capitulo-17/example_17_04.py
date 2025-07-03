# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_04.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

from package.vehicle_display_module import Vehicle

print('A execução do sistema informático foi iniciada.\n')

print("Olá! Vamos construir a classe Veículo com seus atributos e métodos, além de implementar uma função que leia dados de veículos de um arquivo e exiba essas informações formatadas na tela:\n")

dictionary_of_vehicles = {}
for value in open('C:\curso-de-python-modulo-avancado\capitulo-17\example_17_04.txt', 'r'):
    value = value.split(';')
    vehicle = Vehicle(value[0], value[1], int(value[2]), int(value[3]))
    dictionary_of_vehicles[value[0]] = vehicle

print(f'Exibindo os elementos presentes no arquivo: ')
for vehicle in dictionary_of_vehicles.values():
    vehicle.display()

print(f'A execução do sistema informático foi concluída.')