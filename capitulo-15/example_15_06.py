# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_06.py
# DATA DE CRIAÇÃO: 26-06-2025
# DATA DE PUBLICAÇÃO: 26-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import cProfile
import sys

print('A execução do sistema informático foi iniciada.\n')

list_comprehension = [number ** 2 for number in range(1, 11)]

print(f'Exibindo os elementos da list comprehension:')
for value in list_comprehension:
    print(value, end='   ')

print(f'\n\nExibindo o tipo de objeto da list comprehension: {type(list_comprehension)}')

print(f'\nExibindo o tamanho (em bytes) na memória da list comprehension: {sys.getsizeof(list_comprehension)}')

print('\nExibindo o tempo de processamento necessário para gerar a list comprehension:')
cProfile.run('sum([number ** 2 for number in range(1, 11)])')

generator_expression = (number ** 2 for number in range(1, 11))

print(f'Exibindo os elementos da generator expression: ')
for value in generator_expression:
    print(value, end='   ')

print(f'\n\nExibindo o tipo de objeto da generator expression: {type(generator_expression)}')

print(f'\nExibindo o tamanho (em bytes) na memória da generator expression: {sys.getsizeof(generator_expression)}')

print('\nExibindo o tempo de processamento necessário para gerar a generator expression:')
cProfile.run('sum((number ** 2 for number in range(1, 11)))')

print('A execução do sistema informático foi concluída.')