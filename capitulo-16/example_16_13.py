# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_13.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import package.boolean_utilities_module
import package.text_utilities_module

print('A execução do sistema informático foi iniciada.\n')

value = 19

print(package.boolean_utilities_module.message)
print(f'{package.boolean_utilities_module.check_parity(value)}')
print(f'{package.boolean_utilities_module.check_prime_number(value)}')

print(f'\n{package.text_utilities_module.message}')
print(f'{package.text_utilities_module.check_parity(value)}')
print(f'{package.text_utilities_module.check_prime_number(value)}')

print(f'\nA execução do sistema informático foi concluída.')