# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_08.py
# DATA DE CRIAÇÃO: 27-06-2025
# DATA DE PUBLICAÇÃO: 27-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para produzir uma sequência de números:\n')

def generate_numbers():
    number = 10
    while True:
        yield number
        number += 10
 
generator = generate_numbers()
print('Gerando e exibindo cinco elementos através da função gera números:')
for value in range(5):
    print(next(generator), end='   ')

# generator.throw(Exception('A execução do gerador foi encerrada pelo usuário!'))
# print(next(generator), end='   ')

# generator = generate_numbers()
# print('\n\nGerando e exibindo cinco elementos através da função gera números:')
# for value in generator:
    # print(value, end='   ')
    # if value > 40:
        # generator.throw(ValueError('Todos os elementos foram gerados através da função gera números!'))

generator = generate_numbers()
for value in range(0):
    print(next(generator), end='   ')

generator.close()
# print(next(generator), end='   ')

generator = generate_numbers()
print('\n\nGerando e exibindo cinco elementos através da função gera números:')
for value in generator:
    print(value, end='   ')
    if value >= 50:
        generator.close()

# print(next(generator), end='   ')

print(f'\n\nA execução do sistema informático foi concluída.')