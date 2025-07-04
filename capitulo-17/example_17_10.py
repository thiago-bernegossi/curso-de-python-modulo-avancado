# ---------------------------------------------------------------------------------------------------------------------
# ARQUIVO: example_17_10.py
# DATA DE CRIAÇÃO: 04-07-2025
# DATA DE PUBLICAÇÃO: 04-07-2025
# CONTEUDISTA: Faculdade de Tecnologia (FATEC) do Estado de São Paulo
# CONTEÚDO OFERTADO: Curso de Python – Módulo Avançado
# DOCENTE AUTOR: Sérgio Luiz Banin
# DISCENTE: Thiago Bernegossi
# DESCRIÇÃO: Arquivo que contém código-fonte desenvolvido na linguagem de programação Python para fins de aprendizado.
# ---------------------------------------------------------------------------------------------------------------------

print('A execução do sistema informático foi iniciada.\n')

class Music:
    def __init__(self, title, artist, album, year, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre

    def display(self):
        message = 'Música: {}\nArtista: {}\nÁlbum: {}\nAno de lançamento: {}\nGênero: {}'
        print(f'{message.format(self.title, self.artist, self.album, self.year, self.genre)}\n')

music_01 = Music('Time', 'Pink Floyd', 'The Dark Side of the Moon', 1973, 'Rock')
music_02 = Music('Óculos', 'Paralamas do Sucesso', 'O Passo do Lui', 1984, 'MPB')
music_03 = Music('Evidências', 'Chitãozinho e Xororó', 'Cowboy do Asfalto', 1990, 'Sertanejo')

print(f'Música: {music_01.title}')
print(f'Música: {music_02.title}')
print(f'Música: {music_03.title}\n')

music_01.display()
music_02.display()
music_03.display()

print(f'A execução do sistema informático foi concluída.')