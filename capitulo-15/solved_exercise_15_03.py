# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_15_03.py
# DATA DE CRIAÇÃO: 29-06-2025
# DATA DE PUBLICAÇÃO: 29-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 03:
# Reescreva a função geradora do exercício resolvido 15.2 de modo que ela possa receber um inteiro através de uma expressão yield.
# Esse inteiro deve ser usado para resetar o valor inicial para o qual calcularemos o fatorial.
# No programa principal leia a quantidade de tuplas a serem geradas e faça um laço para gerar várias sequências e assim verificar se os retornos da função geradora estão corretos.

# Resolução do Exercício 03:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para produzir uma sequência de números naturais e seus fatoriais correspondentes:\n')

def calculate_factorial():
    number, factorial = 0, 1
    while True:
        value = (yield number, factorial)
        number += 1
        factorial *= number
        if value is not None:
            number, factorial = value, 1
            for new_value in range(1, number + 1):
                factorial *= new_value

numbers = int(input('Digite a quantidade de fatoriais: '))
generator = calculate_factorial()
next(generator)

initial_value = int(input('Digite o valor inicial para os fatoriais: '))
while initial_value >= 0:
    result = generator.send(initial_value)
    factorials = [result]
    for value in range(numbers - 1):
        factorials.append(next(generator))

    print('\nO resultado é:')
    print(f'Gerando e exibindo números naturais e seus fatoriais correspondentes através da função geradora:')
    print(factorials)

    initial_value = int(input('\nDigite o valor inicial para os fatoriais: '))

print(f'\nA execução do sistema informático foi concluída.')