# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_01.py
# DATA DE CRIAÇÃO: 30-06-2025
# DATA DE PUBLICAÇÃO: 30-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import os
import utilities_module

print('A execução do sistema informático foi iniciada.\n')

print(f'O diretório de trabalho atual é: {os.getcwd()}\n')

print(f'{utilities_module.message}\n')

print(f'O meses do ano são: {utilities_module.months}\n')

print(f'{utilities_module.check_parity(25)}\n')

print(f'{utilities_module.check_parity(50)}\n')

print(f'{utilities_module.check_prime_number(10)}\n')

print(f'{utilities_module.check_prime_number(29)}')

print(f'\nA execução do sistema informático foi concluída.')