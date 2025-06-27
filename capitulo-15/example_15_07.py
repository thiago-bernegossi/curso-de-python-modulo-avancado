# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_07.py
# DATA DE CRIAÇÃO: 26-06-2025
# DATA DE PUBLICAÇÃO: 26-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora para produzir uma sequência de números pares ou ímpares:\n')

def generate_numbers():
    number = 2
    remainder = 0
    while True:
        if number % 2 == remainder:
            value = (yield number) 
            if value is not None:
                if value not in (0, 1):
                    raise ValueError('A função recebe apenas os valores 0 ou 1!')
                remainder = value 
                number = 0 
        number += 1
 
generator = generate_numbers()

print('Gerando e exibindo cinco elementos pares através da função gera números:')
for value in range(5):
    print(next(generator), end='   ')
 
print('\n\nGerando e exibindo cinco elementos ímpares através da função gera números:')
result = generator.send(1)
print(result, end='   ')
for value in range(4):
    print(next(generator), end='   ')

print('\n\nGerando e exibindo dez elementos pares através da função gera números:')
result = generator.send(0)
print(result, end='   ')
for value in range(9):
    print(next(generator), end='   ')
 
# result = generator.send(2)
 
print(f'\n\nA execução do sistema informático foi concluída.')