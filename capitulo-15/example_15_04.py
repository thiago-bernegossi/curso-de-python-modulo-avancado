# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_04.py
# DATA DE CRIAÇÃO: 25-06-2025
# DATA DE PUBLICAÇÃO: 25-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora que realize um filtro em um determinado intervalo numérico:\n')

def filter_numbers(numbers, minimum_value, maximum_value):
    for value in numbers:
        if minimum_value <= value <= maximum_value:
            yield value, value * 1.1
        
values = [123.45, 67.89, 145.01, 9.87, 112.34, 30.56, 88.22, 10.03, 137.90, 55.66]
new_minimum_value = float(input('Digite o valor mínimo: '))
new_maximum_value = float(input('Digite o valor máximo: '))

print('\nO resultado é:')
for values in filter_numbers(values, new_minimum_value, new_maximum_value):
    print(values)
          
print(f'\nA execução do sistema informático foi concluída.')