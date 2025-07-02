# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_14.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import package.boolean_utilities_module as boolean_m
import package.text_utilities_module as text_m

print('A execução do sistema informático foi iniciada.\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python (exceto os elementos com "__"):')
for value in dir():
    if '__' not in value:
        print(value)

value = 19

print(f'\n{boolean_m.message}')
print(f'{boolean_m.check_parity(value)}')
print(f'{boolean_m.check_prime_number(value)}')

print(f'\n{text_m.message}')
print(f'{text_m.check_parity(value)}')
print(f'{text_m.check_prime_number(value)}')

print(f'\nA execução do sistema informático foi concluída.')