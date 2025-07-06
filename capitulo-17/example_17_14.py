# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_14.py
# DATA DE CRIAÇÃO: 05-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

import sys
sys.path.append('C:\\curso-de-python-modulo-avancado\\capitulo-17\\package')
from new_vehicle_display_module import Vehicle

vehicle = Vehicle('CMT7153','ONIX LT 1.0',2021,54600)

print(vehicle)

vehicle.display()

print(f'Exibindo a quantidade de instâncias armazenadas na classe Veículo: {len(vehicle)}')

print(f'\nA execução do sistema informático foi concluída.')