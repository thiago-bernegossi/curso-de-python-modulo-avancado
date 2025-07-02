# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: text_utilities_module.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

message = 'Neste módulo, cada função gera e exibe saídas em formato de texto:'

def check_parity(value):
    if value % 2 == 0:
        return f'O número {value} é par!'
    else:
        return f'O número {value} é ímpar!'

def check_prime_number(prime_number):
    if prime_number == 2:
        return f'O número {prime_number} é primo!'
    elif prime_number % 2 == 0:
        return f'O número {prime_number} não é primo!'
    else:
        square_root = pow(prime_number, 0.5)
        remainder = value = 3
        while value <= square_root and remainder != 0:
            remainder = prime_number % value
            value += 2
        if remainder != 0:
            return f'O número {prime_number} é primo!'
        else:
            return f'O número {prime_number} não é primo!'