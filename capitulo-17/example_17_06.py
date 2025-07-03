# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_06.py
# DATA DE CRIAÇÃO: 03-07-2025
# DATA DE PUBLICAÇÃO: 03-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class MyClass:
    def __init__(self, value):
        self.value = value

    def __do_something(self):
        print(f'Após a execução, o primeiro método tem o valor de: {self.value}\n')

    def display_value(self):
        print(f'Após a execução, o segundo método tem o valor de: {self.value}\n')

print('Exibindo a lista de todos os nomes de atributos e métodos disponíveis na classe Minha Classe:')
print(f'{dir(MyClass)}\n')

object_x = MyClass(25)
object_x.display_value()

# object_x.__do_something()

object_x._MyClass__do_something()

class MyClass:
    def __init__(self, value):
        self.value = value

    def _do_something(self):
        print(f'Após a execução, o primeiro método tem o valor de: {self.value}\n')

    def display_value(self):
        print(f'Após a execução, o segundo método tem o valor de: {self.value}\n')

print('Exibindo a lista de todos os nomes de atributos e métodos disponíveis na classe Minha Classe:')
print(f'{dir(MyClass)}\n')

class MyClass:
    def __init__(self, value):
        self.value = value

    def __do_something__(self):
        print(f'Após a execução, o primeiro método tem o valor de: {self.value}\n')

    def display_value(self):
        print(f'Após a execução, o segundo método tem o valor de: {self.value}\n')

print('Exibindo a lista de todos os nomes de atributos e métodos disponíveis na classe Minha Classe:')
print(f'{dir(MyClass)}')

print(f'\nA execução do sistema informático foi concluída.')