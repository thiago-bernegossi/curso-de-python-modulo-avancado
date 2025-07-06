# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_13.py
# DATA DE CRIAÇÃO: 05-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sys
sys.path.append('C:\\curso-de-python-modulo-avancado\\capitulo-17\\package')
from rectangle_calculation_module import Rectangle

print('A execução do sistema informático foi iniciada.\n')

first_rectangle = Rectangle(12, 5)
print('Primeiro retângulo: ', end='')
first_rectangle.display()

first_rectangle.width = 8
print('Primeiro retângulo: ', end='')
first_rectangle.display()

first_rectangle = Rectangle(12, -5)
print('Primeiro retângulo: ', end='')
first_rectangle.display()

# first_rectangle.width = -8
# print('Primeiro retângulo: ', end='')
# first_rectangle.display()

# first_rectangle.width = 'Olá, Mundo!'
# print('Primeiro retângulo: ', end='')
# first_rectangle.display()

second_rectangle = Rectangle(3.5, 9.0)
print('Segundo retângulo: ', end='')
second_rectangle.display()

# second_rectangle = Rectangle(-3.5, 9.0)
# print('Segundo retângulo: ', end='')
# second_rectangle.display()

# second_rectangle = Rectangle(0, 9.0)
# print('Segundo retângulo: ', end='')
# second_rectangle.display()

second_rectangle = Rectangle(3.5, -9.0)
print('Segundo retângulo: ', end='')
second_rectangle.display()

print(f'A execução do sistema informático foi concluída.')