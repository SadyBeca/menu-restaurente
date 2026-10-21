class ItemCardapio: # Classe mãe, as outras dependem dela
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco