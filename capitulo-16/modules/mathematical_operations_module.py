# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: mathematical_operations_module.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

def multiplication(* values):
    product = 1
    for value in values:
        product *= value
    return f'O resultado da multiplicação dos números é: {product}\n'

def sum(* values):
    sum = 0
    for value in values:
        sum += value
    return f'O resultado da soma dos números é: {sum}\n'

if __name__ == '__main__':
    print('\nIniciando a execução do módulo de operações matemáticas...\n')