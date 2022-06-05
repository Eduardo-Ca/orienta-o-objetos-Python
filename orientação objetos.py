class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self) :
        return f'Nome: {self._nome} - Ano: {self.ano} -  Likes: {self._likes}'
    

class Filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self) :
      return  f'Nome: {self._nome} - Ano: {self.ano} - Duração: {vingadores.duracao} -  Likes: {self._likes}'
        

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self) :
       return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {atlanta.temporadas} -  Likes: {self._likes}'

class playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def __len__(self):
        return len(self._programas)
     


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

tmep = Filme("todo mundo em pânico", 199 ,100)
tmep.dar_like()
tmep.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()


demolidor = Serie('demolidor', 2016, 2)

filmes_series = [vingadores,tmep,demolidor,atlanta]
playlist_fim_de_semana = playlist("fim de semana",filmes_series)


print("-="*30)
print(f"tamanho da lista: {len(playlist_fim_de_semana.listagem)}")
print("-="*30)

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print("-="*30)