# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_06.py
# DATA DE CRIAÇÃO: 01-07-2025
# DATA DE PUBLICAÇÃO: 01-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

def first_function():
    print('Iniciando a execução da primeira função...')
    if new_value == 'alterar':
        value = 1000
    print(f'O valor armazenado na primeira função é: {value}')

def second_function():
    print('Iniciando a execução da segunda função...')
    global value
    if new_value == 'alterar':
        value = 1000
    print(f'O valor armazenado na segunda função é: {value}')

new_value = 'alterar'
value = 10

print(f'Antes da execução da primeira função, o valor armazenado na parte principal do sistema informático é: {value}.')
first_function()

print(f'Após a execução da primeira função, o valor armazenado na parte principal do sistema informático é: {value}.')

print(f'\nAntes da execução da segunda função, o valor armazenado na parte principal do sistema informático é: {value}.')
second_function()

print(f'Após a execução da segunda função, o valor armazenado na parte principal do sistema informático é: {value}.')

print(f'\nA execução do sistema informático foi concluída.')