from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    idade: int
    email: str

    def exibir(self):
        print(f'Meu nome é {self.nome},tenho {self.idade} anos e meu email é: {self.email}')

mano = Cliente(nome = 'Verlã', idade = 51, email = 'eskurinhoes@gmail.com')
mano.exibir()
