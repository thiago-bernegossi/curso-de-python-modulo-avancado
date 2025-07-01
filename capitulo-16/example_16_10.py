# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_10.py
# DATA DE CRIAÇÃO: 01-07-2025
# DATA DE PUBLICAÇÃO: 01-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

from utilities_module import check_parity

print(f'\n{check_parity(25)}\n')

print(f'{check_parity(50)}\n')

from utilities_module import check_prime_number

print(f'{check_prime_number(10)}\n')

print(f'{check_prime_number(29)}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

from random import randint

print(f'\nCalculando e exibindo um número inteiro aleatório: {randint(10, 20)}\n')

print(f'Calculando e exibindo um número inteiro aleatório: {randint(10, 20)}\n')

print(f'Calculando e exibindo um número inteiro aleatório: {randint(10, 20)}\n')

print(f'Calculando e exibindo um número inteiro aleatório: {randint(10, 20)}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

print(f'\nA execução do sistema informático foi concluída.')