# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_06.py
# DATA DE CRIAÇÃO: 07-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_06.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql = """
    UPDATE product
    SET cost_price = ?, icms_rate = ?, minimum_stock_quantity = ?
    WHERE code = ?
    """

file_path = 'C:\\curso-de-python-modulo-avancado\\capitulo-18\\example_18_06.txt'
for line in open(file_path, 'r', encoding='utf-8'):
    data = line.split(';')
    data.append(data[0])
    del(data[0])
    print(data)
    cursor.execute(sql, data)
connector.commit()

print('\nOs dados da tabela produto foram atualizados!')

cursor.close()
connector.close()

print('\nA execução do sistema informático foi concluída.')