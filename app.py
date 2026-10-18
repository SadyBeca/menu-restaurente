
from modelos.restaurante import Restaurante

rest_praca = Restaurante('Praça', 'Gourmet')
# rest_mex = Restaurante('Mex Food', 'Mexicana')
# rest_jap = Restaurante('Orient fast', 'Japonesa')

rest_praca.alternar_estado()
rest_praca.receber_avaliacao('Ana', '10')
rest_praca.receber_avaliacao('Matheus', '8')
rest_praca.receber_avaliacao('Igot', '7')

def main():
    Restaurante.listar_restaurantes()  

if __name__ == '__main__':
    main()
