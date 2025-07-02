# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_02.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def display(self):
        print(f'\nO retângulo possui largura de {self.width} e altura de {self.height}, resultando em área de {self.calculate_area():.2f}\n')

first_rectangle = Rectangle(12, 5)
print('Primeiro retângulo: ', end='')
first_rectangle.display()

second_rectangle = Rectangle(3.5, 9.0)
print('Segundo retângulo: ', end='')
second_rectangle.display()

second_rectangle.width = 9.5
second_rectangle.height = 16.3

print('Acessando, de forma isolada, cada atributo e cada método de uma instância:')
print(f'O retângulo possui largura de {second_rectangle.width} e altura de {second_rectangle.height}, resultando em área de {second_rectangle.calculate_area()}')

print(f'\nA execução do sistema informático foi concluída.')