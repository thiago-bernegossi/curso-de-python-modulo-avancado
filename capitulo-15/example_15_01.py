# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_01.py
# DATA DE CRIAÇÃO: 24-06-2025
# DATA DE PUBLICAÇÃO: 24-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

generator_01 = generate_numbers()

print(f'Exibindo o tipo de objeto do gerador 01: {type(generator_01)}\n')

print('Exibindo os valores dos elementos do gerador 01 por meio da iteração do laço de repetição for:')
for value in generator_01:
    print(value)

print('\nExibindo os valores dos elementos da função gera números por meio da iteração do laço de repetição for:')
for value in generate_numbers():
    print(value)

print(f'\nA execução do sistema informático foi concluída.')