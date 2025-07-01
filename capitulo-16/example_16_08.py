# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_08.py
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

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

print('\nExibindo todos os elementos disponíveis no namespace do módulo específico gerado pelo interpretador Python após a inicialização:')
print(dir(utilities_module))

print(f'\n{utilities_module.message}\n')

print(f'O meses do ano são: {utilities_module.months}\n')

print(f'{utilities_module.check_parity(25)}\n')

print(f'{utilities_module.check_parity(50)}\n')

print(f'{utilities_module.check_prime_number(10)}\n')

print(f'{utilities_module.check_prime_number(29)}')

print(f'\nA execução do sistema informático foi concluída.')