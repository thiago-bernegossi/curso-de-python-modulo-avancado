# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_15_04.py
# DATA DE CRIAÇÃO: 29-06-2025
# DATA DE PUBLICAÇÃO: 29-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 04:
# Escreva um programa que implemente uma função geradora capaz de calcular a média móvel de uma sequência de números.
# A média móvel é calculada e apresentada a cada valor que é fornecido.
# Utilize uma função geradora que contenha uma expressão yield e use o método .send() para enviar os valores para a função.
# Exiba os valores com 3 casas decimais.

# Resolução do Exercício 04:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para calcular a média móvel de uma sequência de números reais:\n')

def calculate_moving_average():
    total = number = 0
    while True:
        new_value = (yield total / number if number > 0 else 0)
        if new_value is not None:
            total += new_value
            number += 1

value = input('Digite a quantidade de números reais ou FIM para encerrar: ')
generator = calculate_moving_average()
next(generator)

while value.upper() != 'FIM':
    result = generator.send(float(value))
    print(f'Gerando e exibindo o valor atual da média móvel através da função geradora: {result:.3f}')
    value = input('\nDigite a quantidade de números reais ou FIM para encerrar: ')

print('\nO resultado é:')
print(f'Gerando e exibindo o valor final da média móvel através da função geradora: {result:.3f}')

print(f'\nA execução do sistema informático foi concluída.')