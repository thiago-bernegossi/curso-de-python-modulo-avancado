# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_18_04.py
# DATA DE CRIAÇÃO: 07-07-2025
# DATA DE PUBLICAÇÃO: 07-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sqlite3
connector = sqlite3.connect('C:\\curso-de-python-modulo-avancado\\capitulo-18\\databases\\example_18_04.db')

print('A execução do sistema informático foi iniciada.\n')

cursor = connector.cursor()

sql = """
    INSERT INTO product (code, description, sale_price, stock_quantity)
    VALUES (?, ?, ?, ?);
    """

print('Os dados devem ser separados por vírgulas, sem espaços (Código,Descrição,Preço,Estoque)')
reading_data = input('Digite os dados ou FIM para encerrar: ')

while reading_data.upper() != 'FIM':
    data = reading_data.split(',')
    try:
        print(f'\nOs dados digitados foram: {data}')
        cursor.execute(sql, data)
        connector.commit()
    except:
        print('Os dados digitados são inválidos e não foram incluídos!\n')
    else:
        print('Os dados digitados foram incluídos com sucesso!\n')
    finally:
        print('Os dados devem ser separados por vírgulas, sem espaços (Código,Descrição,Preço,Estoque)')
    reading_data = input('Digite os dados ou FIM para encerrar: ')

cursor.close()
connector.close()

print('\nA execução do sistema informático foi concluída.')