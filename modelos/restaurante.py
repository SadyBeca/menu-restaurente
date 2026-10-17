class Restaurante:
    restaurantes = [] # Variável para conter os objetos
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) # chamo a variável de Restaurante e faço o append de self.

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes(): # Método próprio
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


restaurantes = [restaurante_praca, restaurante_pizza]
print(restaurantes)

Restaurante.listar_restaurantes()

# print(restaurante_praca)
# print(restaurante_pizza)