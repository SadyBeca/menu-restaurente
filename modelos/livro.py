class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicado
        self._disponivel = True
        Livro.livros.append(self)
        

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor} em {self._ano_publicacao} | {self.disponibilidade}'

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'O livro {livro._titulo}, escrito por {livro._autor} em {livro._ano_publicacao} | {livro.disponibilidade}')

    @property
    def disponibilidade(self):
        if self._disponivel:
            return '✅ Disponível para empréstimo'
        else:
            return '❌ Indisponível'

    def emprestar(self):
        self._disponivel = False

    def verificar_disponibilidade(self, ano):
        livros_do_ano = []
        


livro1 = Livro('O estrangeiro', 'Albert Camus', '1960')
livro2 = Livro('Ana Karenina', 'Tolstoi', '1900')

livro2.emprestar()

Livro.listar_livros()