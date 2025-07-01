# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_05.py
# DATA DE CRIAÇÃO: 01-07-2025
# DATA DE PUBLICAÇÃO: 01-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def calculate_sum(object_a, object_b):
    print('\nParte 03-) Exibindo um namespace local do sistema informático:')
    for value in dir():
        print(value)
    return object_a + object_b

def calculate_difference(object_c, object_d):
    print('\nParte 03-) Exibindo um namespace local do sistema informático:')
    for value in dir():
        print(value)
    return object_c - object_d

print('Parte 01-) Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir(__builtins__))

print('\nParte 02-) Exibindo o namespace global do sistema informático (exceto os elementos com "__"):')
first_value = 25
second_value = 15

for value in dir():
    if '__' not in value:
        print(value)

sum = calculate_sum(first_value, second_value)
difference = calculate_difference(first_value, second_value)
print(f'\n{first_value} + {second_value} = {sum}')
print(f'{first_value} - {second_value} = {difference}')

print(f'\nA execução do sistema informático foi concluída.')