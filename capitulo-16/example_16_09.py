# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_09.py
# DATA DE CRIAÇÃO: 01-07-2025
# DATA DE PUBLICAÇÃO: 01-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

utilities_module = 'Este objeto é do tipo string'
print(f'Exibindo os elementos do módulo de utilidades: {utilities_module}')
print(f'Exibindo o tipo de objeto do módulo de utilidades: {type(utilities_module)}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

import utilities_module

print('\nExibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
print(dir(utilities_module))

print(f'\nExibindo os elementos do módulo de utilidades: {utilities_module}')
print(f'Exibindo o tipo de objeto do módulo de utilidades: {type(utilities_module)}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

# utilities_module = 'Este objeto é do tipo string'
# import numpy as utilities_module
# print(f'Exibindo os elementos do módulo de utilidades: {utilities_module}')
# print(f'Exibindo o tipo de objeto do módulo de utilidades: {type(utilities_module)}')

print(f'\nA execução do sistema informático foi concluída.')