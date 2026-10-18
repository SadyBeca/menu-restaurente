class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        if self._ativo:
            return f'Olá {self._titular}, o seu saldo é {self._saldo} e sua {self.ativo} '
        else:
            return f'Olá {self._titular}, sua conta está inativa ❌, com saldo residual de {self._saldo}'

    @property
    def ativo(self):
        return 'Conta Ativa ✅' if self._ativo else 'Conta Inativa ❌'

    @property
    def titular(self):
        return(f'O titular dessa conta é {self._titular}')        

    def ativar_conta(self):
        self._ativo = True


pessoa1 = ContaBancaria('Arthur', '300.0')
pessoa2 = ContaBancaria('Ana', '1000.0')

pessoa2.ativar_conta()

print(pessoa2.ativo, pessoa2.titular)

# print(pessoa1)
# print(pessoa2)

class ClienteBanco:
    def __init__(self, nome, idade, agencia, conta, saldo):
        self._nome = nome.title()
        self._idade = int(idade)
        self._agencia = str(agencia)
        self._conta = str(conta)
        self._saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        return f'Olá, o titular da conta é {self._nome} e seu saldo é de {self._saldo}'

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta


pessoa3 = ClienteBanco('Jorge', '20', '55', '40', '500.0')
pessoa4 = ClienteBanco('Isabela', '19', '40', '90', '400.0')

conta_p3 = ClienteBanco.criar_conta('Ana', '500.0')

print(conta_p3.titular)

