# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_09.py
# DATA DE CRIAÇÃO: 04-07-2025
# DATA DE PUBLICAÇÃO: 04-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Attribute:
    class_attribute = 9.99

    def __init__(self, first_attribute, second_attribute):
        self.first_attribute = first_attribute
        self.second_attribute = second_attribute

    def display_value(self):
        self.third_attribute = 999
        print(f'Exibindo o valor do atributo da classe: {self.class_attribute}\n\n' +
            f'Exibindo o valor do primeiro atributo de instância: {self.first_attribute}\n' +
            f'Exibindo o valor do segundo atributo de instância: {self.second_attribute}\n' +
            f'Exibindo o valor do terceiro atributo de instância: {self.third_attribute}\n')

object_01 = Attribute(10, 'Texto do objeto 01')
object_02 = Attribute(20, 'Texto do objeto 02')

object_01.display_value()
object_02.display_value()

object_01.first_attribute
object_02.first_attribute

object_01.second_attribute
object_02.second_attribute

object_01.class_attribute
object_02.class_attribute

object_01.display_value()
object_02.display_value()

print('Exibindo a lista de todos os nomes de atributos e métodos disponíveis na classe Atributo:')
print(f'{dir(Attribute)}\n')

Attribute.class_attribute = 1250
print(f'Exibindo o valor do atributo da classe após alteração: {Attribute.class_attribute}\n')

object_01.display_value()
object_02.display_value()

object_01.class_attribute = 10
object_01.display_value()

print(f'Exibindo o valor do atributo da classe: {Attribute.class_attribute}\n')

object_01.class_attribute
object_02.class_attribute

object_01 = Attribute(10, 'Texto do objeto 01')
object_01.display_value()

print(f'A execução do sistema informático foi concluída.')