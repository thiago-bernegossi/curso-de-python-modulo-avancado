# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_03.py
# DATA DE CRIAÇÃO: 24-06-2025
# DATA DE PUBLICAÇÃO: 24-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def generate_even_numbers():
    even_number = 2
    while True:
        yield even_number
        even_number += 2

generator_01 = generate_even_numbers()

print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')

print(f'Exibindo o tipo de objeto do gerador 01: {type(generator_01)}\n')

for value in range(10):
    print(f'{next(generator_01)}', end='   ')

generator_02 = generate_even_numbers()

print(f'\n\nExibindo o tipo de objeto do gerador 02: {type(generator_02)}\n')

for value in range(5):
    print(f'{next(generator_02)}', end='   ')
          
print(f'\n\nA execução do sistema informático foi concluída.')