
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

rest_praca = Restaurante('Praça', 'Gourmet')
# rest_mex = Restaurante('Mex Food', 'Mexicana')
# rest_jap = Restaurante('Orient fast', 'Japonesa')

bebida_suco = Bebida('Suco de Laranja', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor paozinho')


def main():
    print(bebida_suco, prato_paozinho)

if __name__ == '__main__':
    main()
