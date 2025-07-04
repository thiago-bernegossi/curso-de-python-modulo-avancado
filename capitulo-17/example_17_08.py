# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_08.py
# DATA DE CRIAÇÃO: 03-07-2025
# DATA DE PUBLICAÇÃO: 04-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Product:
    def __init__(self, barcode, product_name):
        self.barcode = barcode
        self.product_name = product_name
        self.quantity_in_stock = 0

    def register_cost(self, product_cost):
        self.product_cost = product_cost

    def display_product(self):
        print(f'\nO produto {self.product_name} possui o código de barras {self.barcode} e o preço de custo é de R$ {self.product_cost:.2f}\n')

prod = Product('1234567891011', 'Arroz 1 kg')

print(f'Exibindo o dicionário de atributos da classe Minha Classe: ')
print(prod.__dict__)

# prod.display_product()

prod.register_cost(7.50)

print(f'\nExibindo o dicionário de atributos da classe Minha Classe: ')
print(prod.__dict__)

prod.display_product()

print(f'A execução do sistema informático foi concluída.')