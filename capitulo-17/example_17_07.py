# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_07.py
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

    def calculate_sum(self):
        object_a = 10
        self.object_b = 5
        print(f'\nApós a execução, o método tem o valor de: {self.value + object_a + self.object_b}')

first_value = MyClass(23)

print('Exibindo o dicionário de atributos do objeto primeiro valor:')
print(first_value.__dict__)

first_value.calculate_sum()

print('\nExibindo o dicionário de atributos do objeto primeiro valor:')
print(first_value.__dict__)

class MyClass:
    def __init__(self, value):
        self.value = value

    def calculate_sum(self):
        object_a = 10
        self.object_b = 5
        self.object_c = 2
        return f'Após a execução, o método tem o valor de: {self.value + object_a + self.object_b}\n'

second_value = MyClass(10)

print('\nExibindo o dicionário de atributos do objeto segundo valor:')
print(second_value.__dict__)

second_value.calculate_sum()

print('\nExibindo o dicionário de atributos do objeto segundo valor:')
print(second_value.__dict__)

print('\nExibindo o dicionário de atributos do objeto primeiro valor:')
print(first_value.__dict__)

print('\nExibindo o dicionário de atributos da classe Minha Classe:')
for value in MyClass.__dict__.items():
    print(value)

print(f'\nExibindo o identificador do método calcular soma: {id(MyClass.calculate_sum)}')

print(f'\nA execução do sistema informático foi concluída.')