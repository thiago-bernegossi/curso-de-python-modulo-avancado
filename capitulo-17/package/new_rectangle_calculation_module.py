# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: new_rectangle_calculation_module.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int | float):
            raise TypeError('A largura e a altura do retângulo devem ser números reais!')
        if value <= 0:
            raise ValueError('A largura e a altura do retângulo devem ser maiores que zero!')
        instance.__dict__[self._name] = value

class Rectangle:
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def calculate_area(self):
        return self.width * self.height

    def display(self):
        print(f'\nO retângulo possui largura de {self.width} e altura de {self.height}, resultando em área de {self.calculate_area():.2f}\n')