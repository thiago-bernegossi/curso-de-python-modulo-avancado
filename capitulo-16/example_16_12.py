# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_12.py
# DATA DE CRIAÇÃO: 01-07-2025
# DATA DE PUBLICAÇÃO: 01-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import utilities_module

print('A execução do sistema informático foi iniciada.\n')

print('Exibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
for value in dir(utilities_module):
    print(value)

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
for value in dir():
    print(value)

from utilities_module import *

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
for value in dir():
    print(value)

print(f'\nA execução do sistema informático foi concluída.')