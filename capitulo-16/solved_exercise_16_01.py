# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: solved_exercise_16_01.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Enunciado do Exercício 01:
# Escreva um programa que exiba na tela o código, o preço de custo e o preço de venda de produtos, sabendo que a margem bruta de lucro aplicada pela empresa é de 16% para a maioria dos produtos.
# Alguns produtos podem ter essa margem reduzida e nesses casos o código do produto tem seu primeiro dígito trocado.
# Quando o primeiro dígito for '8' a margem é 12% e quando esse dígito for '9' a margem é 10%.

# Dados para testes do Exercício 01:
# +--------+---------------+---------------+
# | Código | Preço de custo| Preço de venda|
# +--------+---------------+---------------+
# | 1280   |       100.00  |        116.00 |
# | 8280   |       100.00  |        112.00 |
# | 9280   |       100.00  |        110.00 |
# +--------+---------------+---------------+

# Resolução do Exercício 01:
print('A execução do sistema informático foi iniciada.\n')

print('Olá! Vamos criar uma função para calcular o valor de um produto de acordo com o código, preço de custo, preço de venda e margens pré-definidas:\n')

def calculate_selling_price(product_code, cost_price):
    def adjust_margin():
        nonlocal margin
        if product_code[0] == '8':
            margin = 12 / 100
        elif product_code[0] == '9':
            margin = 10 / 100
    margin = 16 / 100
    adjust_margin()
    selling_price = cost_price * (1 + margin)
    return selling_price

cost_price = 100

product_code = '1280'
print('O resultado é:')
print(f'Código: {product_code} | Preço de custo: {cost_price:.2f} | Preço de venda: {calculate_selling_price(product_code, cost_price):.2f}')

product_code = '8280'
print(f'Código: {product_code} | Preço de custo: {cost_price:.2f} | Preço de venda: {calculate_selling_price(product_code, cost_price):.2f}')

product_code = '9280'
print(f'Código: {product_code} | Preço de custo: {cost_price:.2f} | Preço de venda: {calculate_selling_price(product_code, cost_price):.2f}')

print(f'\nA execução do sistema informático foi concluída.')