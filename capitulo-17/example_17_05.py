# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_05.py
# DATA DE CRIAÇÃO: 03-07-2025
# DATA DE PUBLICAÇÃO: 03-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

list_01 = [2, 4, 6, 8]
print('Exibindo todos os atributos e métodos disponíveis para o objeto lista 01:')
print(dir(list_01))

# print(list_01.__sizeof__())

list_01.append(10)
list_01.append(12)

print(f'\nExibindo a quantidade de elementos da lista 01 através de um método não público: {list_01.__len__()}')
print(f'Exibindo a quantidade de elementos da lista 01 através de uma função embutida: {len(list_01)}')

# print(list_01.__sizeof__())

print(f'\nA execução do sistema informático foi concluída.')