# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_15_01.py
# DATA DE CRIAÇÃO: 27-06-2025
# DATA DE PUBLICAÇÃO: 27-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva uma função geradora capaz de calcular e retornar números primos a partir do 2.
# Escreva um programa para testá-la.

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para produzir uma sequência de números primos a partir do número dois:\n')

def generate_prime_number(): 
    yield 2
    value = 3
    while True:
        square_root = value ** 0.5
        iterator = 3
        while iterator <= square_root and value % iterator != 0:
            iterator += 2
        if iterator > square_root:
            yield value
        value += 2

generator = generate_prime_number()
numbers = int(input('Digite a quantidade de números primos: '))

print('\nO resultado é:')
print(f'Gerando e exibindo {numbers} número(s) primo(s) através da função geradora:')
for value in range(numbers):
    print(next(generator), end='   ')
 
print(f'\n\nA execução do sistema informático foi concluída.')