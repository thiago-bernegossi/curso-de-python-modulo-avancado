# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_14_02.py
# DATA DE CRIAÇÃO: 23-06-2025
# DATA DE PUBLICAÇÃO: 23-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva uma função que recebe uma lista ou tupla com valores numéricos e retorne uma lista contendo o quadrado dos valores recebidos.
# Utilize exceções para as situações de possível erro.

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que recebe uma lista ou tupla de números e retorna uma nova lista com o quadrado de cada número:\n')

def square_numbers_in_sequence(numbers):
    if not isinstance(numbers, list | tuple):
        raise TypeError('A função recebe apenas uma lista ou tupla de números!')   
    if not all(isinstance(number, int | float) for number in numbers):
        raise ValueError('A função recebe apenas valores numéricos!')
    return [value ** 2 for value in numbers]

list_01 = [2.5, 5, 7.5, 10]

print('O resultado é:')
print(square_numbers_in_sequence(list_01))

print(f'\nA execução do sistema informático foi concluída.')