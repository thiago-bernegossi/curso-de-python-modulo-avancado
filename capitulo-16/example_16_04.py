# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_16_04.py
# DATA DE CRIAÇÃO: 30-06-2025
# DATA DE PUBLICAÇÃO: 30-06-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

print('Exibindo o namespace global do sistema informático principal gerado pelo interpretador Python após a inicialização:\n')

object_01 = 10
object_02 = 3.45
object_03 = (1, 2, 3, 4, 5)
object_04 = 'Olá, Mundo!'

print('Primeira iteração do laço de repetição for:')
for value in dir():
    print(value)

object_05 = 50

print(f'\nSegunda iteração do laço de repetição for:')
for value in dir():
    print(value)

print(f'\nA execução do sistema informático foi concluída.')