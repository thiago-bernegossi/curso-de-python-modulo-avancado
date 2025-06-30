# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_02.py
# DATA DE CRIAÇÃO: 30-06-2025
# DATA DE PUBLICAÇÃO: 30-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

import sys

print('A execução do sistema informático foi iniciada.\n')

print('A lista de diretórios que o Python pesquisa quando tentamos importar um módulo é:')
for path in sys.path:
    print(path)

print(f'\nA execução do sistema informático foi concluída.')