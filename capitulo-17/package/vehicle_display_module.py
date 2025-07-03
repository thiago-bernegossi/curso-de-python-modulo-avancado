# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: vehicle_display_module.py
# DATA DE CRIAÇÃO: 02-07-2025
# DATA DE PUBLICAÇÃO: 02-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, license_plate, model, year, km):
        self.license_plate = license_plate
        self.model = model
        self.year = year
        self.km = km

    def display(self):
        print(f'O veículo possui placa: {self.license_plate}, modelo: {self.model}, ano: {self.year} e quilometragem: {self.km}\n')