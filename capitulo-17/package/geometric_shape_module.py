# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: geometric_shape_module.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

class GeometricShape:
    def __init__(self):
        self.shape_type = 'A forma geométrica não foi definida!'

    def display_shape_type(self):
        print(self.shape_type)

class Circle(GeometricShape):
    def __init__(self, radius):
        self.shape_type = 'A forma geométrica é um círculo!'
        self.radius = radius

    def display(self):
        super().display_shape_type()
        print(f'O círculo possui raio de {self.radius}\n')

class Rectangle(GeometricShape):
    def __init__(self, width, height):
        self.shape_type = 'A forma geométrica é um retângulo!'
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def display(self):
        super().display_shape_type()
        print(f'O retângulo possui largura de {self.width} e altura de {self.height}, resultando em área de {self.calculate_area():.2f}\n')