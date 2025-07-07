# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_01.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_01.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql = """
    CREATE TABLE product (
        code INTEGER,
        description TEXT,
        sale_price NUMERIC,
        stock_quantity INTEGER
    );
    """
cursor.execute(sql)

sql = """
    INSERT INTO product (code, description, sale_price, stock_quantity)
    VALUES (1138, 'Lápis Grafite HB', 1.90, 376);
    """
cursor.execute(sql)

sql = """
    INSERT INTO product (code, description, sale_price, stock_quantity)
    VALUES (1251, 'Papel Sulfite A4 75G 100 Folhas', 7.25, 188);
    """
cursor.execute(sql)

connector.commit()

cursor.close()
connector.close()

print(f'A execução do sistema informático foi concluída.')