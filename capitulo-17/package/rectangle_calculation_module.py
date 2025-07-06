# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: rectangle_calculation_module.py
# DATA DE CRIAÇÃO: 05-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int | float):
            raise TypeError('A largura do retângulo deve ser um número real!')
        if value <= 0:
            raise ValueError('A largura do retângulo deve ser maior que zero!')
        self._width = value

    def calculate_area(self):
        return self.width * self.height

    def display(self):
        print(f'\nO retângulo possui largura de {self.width} e altura de {self.height}, resultando em área de {self.calculate_area():.2f}\n')