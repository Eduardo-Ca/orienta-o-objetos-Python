from random import randint

#para criar um objeto
class pessoa:

    ano_atual = 2022

    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self): #metodo
        print(f'{self.nome} está falando.')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo .')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    @classmethod #Métodos de Classes
    def por_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    def get_ano_nascimento(self): #metodo normal
        print(f"nasceu em {self.ano_atual - self.idade}")
    
    @staticmethod #metodo estatico
    def gera_id():
        rand = randint(10000, 19999)
        return rand


#from objeto import pessoa  /importação class pessoa:

p1 = pessoa("luiz",29) #usando objeto

p1.falar() #usando metodo

p1.comer("pizza")


print(p1.nome, p1.idade)
p1 = pessoa.por_ano_nascimento("luiz",1987)
p1.get_ano_nascimento()
print(p1.gera_id())



