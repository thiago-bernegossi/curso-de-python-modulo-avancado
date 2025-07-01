# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_07.py
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

object_a = 123
object_b = 45.6
object_c = "Olá, Mundo!"

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

object_d = 0
del(object_d)

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

import os
import sys
sys.path.append('C:\\curso-de-python-modulo-avancado\\capitulo-16\\modules')
import another_utilities_module

print(f'\nO diretório de trabalho atual é: {os.getcwd()}\n')

print(f'{another_utilities_module.message}\n')

print(f'O meses do ano são: {another_utilities_module.months}\n')

print(f'{another_utilities_module.check_parity(25)}\n')

print(f'{another_utilities_module.check_parity(50)}\n')

print(f'{another_utilities_module.check_prime_number(10)}\n')

print(f'{another_utilities_module.check_prime_number(29)}')

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

print('\nExibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
print(dir(another_utilities_module))

print('\nExibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
for value in dir(another_utilities_module):
    print(value)

print('\nExibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
for value in dir(sys):
    print(value)

print(f'\nA execução do sistema informático foi concluída.')