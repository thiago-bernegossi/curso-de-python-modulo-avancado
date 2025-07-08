# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_05.py
# DATA DE CRIAÇÃO: 07-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_05.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql = 'ALTER TABLE product ADD COLUMN cost_price NUMERIC'
cursor.execute(sql)

sql = 'ALTER TABLE product ADD COLUMN icms_rate NUMERIC'
cursor.execute(sql)

sql = 'ALTER TABLE product ADD COLUMN minimum_stock_quantity NUMERIC'
cursor.execute(sql)

sql = """
    UPDATE product
    SET cost_price = 0,
        icms_rate = 0,
        minimum_stock_quantity = 0
    """
cursor.execute(sql)

connector.commit()

cursor.close()
connector.close()

print('A execução do sistema informático foi concluída.')