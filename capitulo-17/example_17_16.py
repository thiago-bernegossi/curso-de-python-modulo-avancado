# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_16.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sys
sys.path.append('C:\\curso-de-python-modulo-avancado\\capitulo-17\\package')
from geometric_shape_module import *

print('A execução do sistema informático foi iniciada.\n')
 
circle = Circle(5.5) 
circle.display() 
 
rectangle = Rectangle(12, 5)
rectangle.display()
 
rectangle.width = 8
rectangle.height = 8
rectangle.display()

geometric_shape = GeometricShape()
# geometric_shape.display()
geometric_shape.display_shape_type()

print(f'\nA execução do sistema informático foi concluída.')