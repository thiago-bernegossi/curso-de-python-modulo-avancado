# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_03.py
# DATA DE CRIAÇÃO: 07-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_03.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql = """
    SELECT * FROM product
    WHERE code BETWEEN 11000 AND 11999
    ORDER BY description;
    """
cursor.execute(sql)

data = cursor.fetchall()

cursor.close()
connector.close()

print('Consulta ao banco de dados: example_18_03.db')
print('-' * 67)

print('Exibindo os dados da tabela: Produto')
print('-' * 67)

print('{:7}{:44}{:>8}{:>8}'.format('Código', 'Descrição', 'Preço', 'Estoque'))
print('- ' * 34)

for value in data:
    print('{:<7}{:44}{:8.2f}{:8}'.format(
        value[0],
        value[1],
        value[2],
        value[3]
    ))
print('-' * 67)

print('Foram localizados: {} registro(s)'.format(len(data)))
print('-' * 67)

print('\nA execução do sistema informático foi concluída.')