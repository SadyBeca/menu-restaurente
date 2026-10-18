class Pessoa:
    pessoas = []
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao.title()
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.saudacao}, você tem {self._idade} anos'

    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa)
        pass

    @property
    def saudacao(self):
        return f'Olá {self._profissao} {self._nome}!'

    def aniversario(self):
        self._idade += 1
        return f'Parabéns, você tem {self._idade}!'


pessoa1 = Pessoa('Ana', '33', 'Engenheira')
pessoa2 = Pessoa('Carlos', '25', 'Analista')
pessoa3 = Pessoa('Augusto', '50', 'Porteiro')


print(pessoa2.aniversario())

Pessoa.listar_pessoas()