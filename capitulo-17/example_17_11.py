# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_11.py
# DATA DE CRIAÇÃO: 04-07-2025
# DATA DE PUBLICAÇÃO: 04-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Counter:
    instance_counter = 0

    def __init__(self):
        Counter.instance_counter += 1

print(f'Exibindo o valor do atributo da classe: {Counter.instance_counter}\n')

first_object = Counter()
print(f'Após utilizar o construtor da classe Contador e criar o primeiro objeto, o valor do atributo da classe é: {Counter.instance_counter}\n')

print(f'Após utilizar o construtor da classe Contador e criar o primeiro objeto, o valor do atributo da classe acessado pelo primeiro objeto é: {first_object.instance_counter}\n')

second_object = Counter()
print(f'Após utilizar o construtor da classe Contador e criar o segundo objeto, o valor do atributo da classe é: {Counter.instance_counter}\n')

print(f'Após utilizar o construtor da classe Contador e criar o segundo objeto, o valor do atributo da classe acessado pelo segundo objeto é: {first_object.instance_counter}\n')

for value in range(8):
    new_objects = Counter()

print(f'Após utilizar o construtor da classe Contador e criar oito novos objetos, o valor do atributo da classe acessado pelo primeiro objeto é: {first_object.instance_counter}\n')

print(f'Após utilizar o construtor da classe Contador e criar oito novos objetos, o valor do atributo da classe acessado pelo segundo objeto é: {second_object.instance_counter}\n')

print(f'Após utilizar o construtor da classe Contador e criar oito novos objetos, o valor do atributo da classe acessado pela variável novos objetos é: {new_objects.instance_counter}\n')

print(f'A execução do sistema informático foi concluída.')