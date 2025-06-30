# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: utilities_module.py
# DATA DE CRIAÇÃO: 30-06-2025
# DATA DE PUBLICAÇÃO: 30-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

message = 'Este é o módulo utilities_module.py'

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def check_parity(value):
    if value % 2 == 0:
        return f'O número {value} é PAR!'
    else:
        return f'O número {value} é ÍMPAR!'

def check_prime_number(prime_number):
    if prime_number == 2:
        return f'O número {prime_number} é primo: {True}'
    elif prime_number % 2 == 0:
        return f'O número {prime_number} é primo: {False}'
    else:
        square_root = pow(prime_number, 0.5)
        value = 3
        while value <= square_root:
            if prime_number % square_root == 0:
                return f'O número {prime_number} é primo: {False}'
            value += 2
        return f'O número {prime_number} é primo: {True}'