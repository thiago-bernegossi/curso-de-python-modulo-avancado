# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_17_01.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que permaneça em laço lendo a base e a altura de retângulos e exibindo na tela sua área, com 3 casas decimais.
# Isso deve ser feito com o uso de uma classe Retangulo contida em um módulo à parte do programa principal.
# O laço termina quando for digitado "FIM".

# Resolução do Exercício 01:
import sys
sys.path.append('C:\\curso-de-python-modulo-avancado\\capitulo-17\\package')
from another_rectangle_calculation_module import Rectangle

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar um laço de repetição que leia a base e a altura de retângulos e exiba sua área com três casas decimais, utilizando uma classe em um módulo separado:\n')

rectangle = Rectangle(0, 0)
value = input('Digite dois valores reais e separados por um espaço (base altura): ')

while value.upper() != 'FIM':
    values = value.split()
    rectangle.width = float(values[0])
    rectangle.height = float(values[1])
    rectangle.display()
    value = input('Digite dois valores reais e separados por um espaço (base altura): ')

print(f'\nA execução do sistema informático foi concluída.')