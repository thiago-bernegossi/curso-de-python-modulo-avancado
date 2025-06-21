# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_14_01.py
# DATA DE CRIAÇÃO: 20-06-2025
# DATA DE PUBLICAÇÃO: 21-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('Olá! Vamos construir uma função que leia um número inteiro e informe se o número é par ou ímpar:\n')

def verify_number(number):
    if not isinstance(number, int):
        raise Exception('A função recebe apenas um número inteiro!') 
    if number % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

number = int(input('Digite um número inteiro: '))
result = verify_number(number)

print('\nO resultado é:')
print(f'O número inteiro digitado e lido pela função é: {result}!')

print(f'\nA execução do sistema informático foi concluída.')