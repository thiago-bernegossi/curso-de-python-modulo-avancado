# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_01.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class MyClass:
    pass

print(f'Exibindo os elementos da classe Minha Classe: {MyClass}')
print(f'Exibindo o tipo de objeto da classe Minha Classe: {type(MyClass)}\n')

print('Exibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

variable_01 = MyClass()

print('\nExibindo a lista de todos os elementos pré-definidos inerentes ao ambiente do interpretador Python:')
print(dir())

print(f'\nExibindo os elementos da variável 01: {variable_01}')
print(f'Exibindo o tipo de objeto da variável 01: {type(variable_01)}')

print(f'\nA execução do sistema informático foi concluída.')