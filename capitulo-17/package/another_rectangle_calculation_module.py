# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: another_rectangle_calculation_module.py
# DATA DE CRIAÇÃO: 06-07-2025
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
  
    def calculate_area(self):
        return self.width * self.height

    def display(self):
        print('\nO resultado é:')
        print(f'O retângulo possui largura de {self.width} e altura de {self.height}, resultando em área de {self.calculate_area():.3f}\n')