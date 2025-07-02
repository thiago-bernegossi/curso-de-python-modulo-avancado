# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_11.py
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

message = '\nEste é o módulo another_utilities_module.py'
print(f'{message}\n')

months = ['Dezembro', 'Novembro', 'Outubro', 'Setembro', 'Agosto', 'Julho', 'Junho', 'Maio', 'Abril', 'Março', 'Fevereiro', 'Janeiro']
print(f'O meses do ano são: {months}\n')

check_parity = 10
print(f'{check_parity}\n')

check_prime_number = 11
print(f'{check_prime_number}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

from utilities_module import message, months, check_parity, check_prime_number

print(f'\n{message}\n')

print(f'O meses do ano são: {months}\n')

print(f'{check_parity(25)}\n')

print(f'{check_parity(50)}\n')

print(f'{check_prime_number(10)}\n')

print(f'{check_prime_number(29)}')

print(f'\nA execução do sistema informático foi concluída.')