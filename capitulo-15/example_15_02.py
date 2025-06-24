# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_02.py
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
    print('Exibindo o valor do primeiro elemento da função gera números:')
    yield 10
    print('Exibindo o valor do segundo elemento da função gera números:')
    yield 20
    print('Exibindo o valor do terceiro elemento da função gera números:')
    yield 30
    print('Exibindo o valor do quarto elemento da função gera números:')
    yield 40
    print('Exibindo o valor do quinto elemento da função gera números:')
    yield 50
    
generator_01 = generate_numbers()

print(f'Exibindo o tipo de objeto do gerador 01: {type(generator_01)}\n')

print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}\n')
print(f'{next(generator_01)}')

print(f'\nA execução do sistema informático foi concluída.')