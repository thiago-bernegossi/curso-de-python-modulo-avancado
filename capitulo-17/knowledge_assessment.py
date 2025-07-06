# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: knowledge_assessment.py
# DATA DE CRIAÇÃO: 06-07-2025
# DATA DE PUBLICAÇÃO: 06-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

# Questão 01-) Considere o código que segue:
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
# Se criado um objeto deste tipo, como segue:
r = Retangulo(0, 0)
# Para atribuir o valor 2.0 para a altura do objeto r definido como acima, podemos escrever:
# Resposta: a. r.altura = 2.0

# Questão 02-) Na Programação Orientada a Objetos (POO), os membros de uma classe são:
# • Atributo, dado necessário ao funcionamento do objeto, definindo seu estado, definido como um objeto dentro da classe.
# • Método, função implementada dentro da classe, que lhe confere uma funcionalidade ou comportamento ao objeto.
# O Python emprega estes conceitos gerais e inclui outros específicos:
# Resposta: a. O corpo de uma classe funciona como um namespace para seus atributos e métodos.