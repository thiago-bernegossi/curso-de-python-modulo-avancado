# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_12.py
# DATA DE CRIAÇÃO: 04-07-2025
# DATA DE PUBLICAÇÃO: 04-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Example:
    first_attribute = 'Azul'
    second_attribute = 'Laranja'

    def __init__(self, value):
        self.value = value

first_object = Example(125)

print(f'Exibindo o dicionário de atributos de instância do primeiro objeto: {first_object.__dict__}')

print(f'\nApós utilizar o construtor da classe Exemplo e criar o primeiro objeto, o valor do primeiro atributo da classe acessado pelo primeiro objeto é: {first_object.first_attribute}\n')
print(f'Após utilizar o construtor da classe Exemplo e criar o primeiro objeto, o valor do segundo atributo da classe acessado pelo primeiro objeto é: {first_object.second_attribute}\n')

second_object = Example(3.75)

print(f'Exibindo o dicionário de atributos de instância do segundo objeto: {second_object.__dict__}')

print(f'\nApós utilizar o construtor da classe Exemplo e criar o segundo objeto, o valor do primeiro atributo da classe acessado pelo segundo objeto é: {second_object.first_attribute}\n')
print(f'Após utilizar o construtor da classe Exemplo e criar o segundo objeto, o valor do segundo atributo da classe acessado pelo segundo objeto é: {second_object.second_attribute}\n')

print(f'Exibindo o dicionário de atributos da classe Exemplo: ')
for value in Example.__dict__.items():
    print(value)

Example.first_attribute = 'Maçã'
Example.second_attribute = 'Verde'

print(f'\nExibindo o valor do primeiro atributo da classe: {Example.first_attribute}\n')
print(f'Exibindo o valor do segundo atributo da classe: {Example.second_attribute}\n')

print(f'Exibindo o valor do primeiro atributo da classe acessado pelo primeiro objeto: {first_object.first_attribute}\n')
print(f'Exibindo o valor do segundo atributo da classe acessado pelo primeiro objeto: {first_object.second_attribute}\n')

print(f'Exibindo o valor do primeiro atributo da classe acessado pelo segundo objeto: {second_object.first_attribute}\n')
print(f'Exibindo o valor do segundo atributo da classe acessado pelo segundo objeto: {second_object.second_attribute}\n')

print(f'Exibindo o dicionário de atributos da classe Exemplo: ')
for value in Example.__dict__.items():
    print(value)

print(f'\nExibindo o dicionário de atributos de instância do primeiro objeto: {first_object.__dict__}')

print(f'\nExibindo o dicionário de atributos de instância do segundo objeto: {second_object.__dict__}')

first_object.first_attribute = 'Abacaxi'

print(f'\nExibindo o dicionário de atributos de instância do primeiro objeto após alteração: {first_object.__dict__}')

print(f'\nExibindo o valor do primeiro atributo da classe acessado pelo primeiro objeto após alteração: {first_object.first_attribute}')

del(first_object.first_attribute)

print(f'\nExibindo o dicionário de atributos de instância do primeiro objeto: {first_object.__dict__}')

print(f'\nExibindo o valor do primeiro atributo da classe acessado pelo primeiro objeto: {first_object.first_attribute}\n')

print(f'A execução do sistema informático foi concluída.')