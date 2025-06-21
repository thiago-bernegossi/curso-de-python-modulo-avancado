# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_14_01.py
# DATA DE CRIAÇÃO: 21-06-2025
# DATA DE PUBLICAÇÃO: 21-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que verifique se um número inteiro lido é primo.
# Faça isso usando uma função e utilize exceções para controlar os erros.
# O parâmetro da função deve ser um número inteiro maior ou igual a 2.
# Se esse parâmetro for menor que dois use a exceção ValueError.
# Se esse parâmetro for de classe diferente de número inteiro use a exceção TypeError.

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função que leia um número inteiro e informe se ele é um número primo:\n')

def verify_prime_number(prime_number):
    if type(prime_number) != int:
        raise TypeError('A função recebe apenas um número inteiro!')
    if prime_number < 2:
        raise ValueError('A função recebe apenas um valor maior ou igual a 2!')
    if prime_number == 2:
        return True
    elif prime_number % 2 == 0:
        return False
    else:
        square_root = pow(prime_number, 0.5)
        value = 3
        while value <= square_root:
            if prime_number % square_root == 0:
                return False
            value += 2
        return True

try:
    number = int(input('Digite um número inteiro: '))

    print('\nO resultado é:')
    if verify_prime_number(number): 
        print(f'O número {number} é primo') 
    else: 
        print(f'O número {number} não é primo')
except TypeError as first_message:
    print(f'Erro: {first_message}')
except ValueError as second_message:
    print(f'Erro: {second_message}')

print(f'\nA execução do sistema informático foi concluída.')