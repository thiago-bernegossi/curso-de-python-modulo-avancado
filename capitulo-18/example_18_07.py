# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_07.py
# DATA DE CRIAÇÃO: 07-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_07.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql_check = 'SELECT COUNT(code) FROM product WHERE code = ?'
sql_delete = 'DELETE FROM product WHERE code = ?'
deleted_codes = []

code = input('Digite o código do produto que será excluído: ')
while code.upper() != 'FIM':
    cursor.execute(sql_check, [int(code)])
    value = cursor.fetchone()
    if value[0] == 0:
        print(f'\nNenhum produto encontrado com o código {code}!\n')
    else:
        cursor.execute(sql_delete, [int(code)])
        deleted_codes.append(int(code))
    code = input('Digite o código do produto que será excluído: ')
connector.commit()

print(f'\nOs códigos {deleted_codes} da tabela produto foram excluídos!')

cursor.close()
connector.close()

print('\nA execução do sistema informático foi concluída.')