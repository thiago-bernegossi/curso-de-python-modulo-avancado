# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_15_05.py
# DATA DE CRIAÇÃO: 25-06-2025
# DATA DE PUBLICAÇÃO: 25-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função geradora que leia o conteúdo de um arquivo e, em seguida, exiba os elementos presentes no arquivo na tela:\n')

def read_file(file_name):
    for line in open(file_name, 'r'):
        yield line.rstrip()

file = input('Digite o nome do arquivo: ')

print(f'\nExibindo os elementos presentes no arquivo: ')
for line in read_file(file):
    print(line)

print(f'\nA execução do sistema informático foi concluída.')