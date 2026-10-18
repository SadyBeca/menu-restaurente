from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = [] # Variável para conter os objetos
    def __init__(self, nome, categoria):
        self._nome = nome.title() # Primeira letra maiúscula
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # chamo a variável de Restaurante e faço o append de self.

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls): # Método próprio
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliação'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(24)} | {str(restaurante.media_avaliacoes)}')

    @property
    def ativo(self):
        return '✅ Ativo' if self._ativo else '❌ Inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        else:
            soma_das_notas = sum(float(avaliacao._nota) for avaliacao in self._avaliacao)
            qte_notas = len(self._avaliacao)
            return round(soma_das_notas/qte_notas, 1)
        

    

# restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_pizza = Restaurante('pizza Express', 'Italiana')
# restaurante_praca.alternar_estado()


# # restaurantes = [restaurante_praca, restaurante_pizza]
# # print(restaurantes)

# Restaurante.listar_restaurantes()

# # print(restaurante_praca)
# # print(restaurante_pizza)