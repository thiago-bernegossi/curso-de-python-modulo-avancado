# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: knowledge_assessment.py
# DATA DE CRIAÇÃO: 23-06-2025
# DATA DE PUBLICAÇÃO: 23-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Questão 01-) Analise o trecho de código que segue:
def func(x):
    if x < 0:
        raise ArithmeticError
    return 2 * x

try:
    x = int(input('Digite um inteiro: '))
    print(f'func({x}) = {func(x)}')
except ArithmeticError:
    print('Erro 1')
except ValueError:
    print('Erro 2')
except Exception:
    print('Erro 3')
# Quais são as mensagens impressas por este código se o usuário fornece os valores 1, 1.0 e -1?
# Resposta: b. func(1) = 2, Erro 2, Erro 1

# Questão 02-) Sobre o tratamento de exceções, considere as afirmativas que seguem:
# I. Levantar uma exceção é a ação de gerar uma exceção em um ponto do programa para que seja tratada em outro.
# II. O levantamento de exceções é feito com a diretiva raise.
# III. A captura de exceções é feita com a diretiva catch.
# Resposta: a. apenas as afirmativas I e II estão corretas.