class Conta:
    def __init__(self, numero:int, saldo:float):
        self.limite = 100
        self.numero = numero
        self.saldo = saldo + self.limite
        self.extrato = []

    def getNumero(self):
       return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor):
        if valor > self.saldo - self.limite:
            self.limite = self.saldo - valor
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(-valor)
            return True
        else:
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(valor)
            if self.limite == 0:
                self.limite += valor
            if self.saldo >= 100:
                self.limite = 100
            return True
        else:
            return False

    def transferir(self, destino, valor:float):
        if destino:
            if 0 < valor <= self.saldo:
                self.sacar(valor)
                destino.depositar(valor)
                return True
            else:
                print('Saldo insuficiente para a transferência.')
                return False



    def verExtrato(self):
            return self.extrato


