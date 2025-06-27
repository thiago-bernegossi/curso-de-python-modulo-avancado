# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_15_02.py
# DATA DE CRIAÇÃO: 27-06-2025
# DATA DE PUBLICAÇÃO: 27-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 02:
# Escreva uma função geradora capaz de calcular e retornar o fatorial de um número natural.
# Essa função deve retornar uma tupla com o próprio número natural e seu fatorial.
# Escreva um programa para testá-la.
# Lembre-se que 0! = 1.

# Resolução do Exercício 02:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para produzir uma sequência de números naturais e seus fatoriais correspondentes:\n')

def calculate_factorial():
    number, factorial = 0, 1
    while True:
        yield number, factorial
        number += 1
        factorial *= number

generator = calculate_factorial()
numbers = int(input('Digite a quantidade de números naturais: '))

print('\nO resultado é:')
print(f'Gerando e exibindo {numbers} números naturais e seus fatoriais correspondentes através da função geradora:')
for value in range(numbers):
    print(next(generator))

print(f'\nA execução do sistema informático foi concluída.')