from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.vagas_normais = self.capacidade - self.qtdPrioritarios
        self.passageiro_normal = [None] * (capacidade - qtdPrioritarios)
        self.passageiro_prioritarios = [None] * qtdPrioritarios
        self.lista_strings = []
        self.vagas = capacidade

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.vagas_normais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < len(self.passageiro_normal):
            return self.passageiro_normal[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if self.passageiro_prioritario.count(None) == 0:
            return self.passageiro_prioritario[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagas

    def subir(self, passageiro: Passageiro):
        if self.passageiro_prioritario.count(None) == 0 and self.passageiro_normal.count(None) == 0:
            print("A topic está lotada, não é possivel subir mais nenhum passageiro")
            return False

        if passageiro.idade >= 65:
            if None in self.passageiro_prioritario:
                index = self.passageiro_prioritario.index(None)
                self.passageiro_prioritario[index] = passageiro
                self.vagas -= 1
                print(
                    f"Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira preferencial {index}.")
                return True

            elif None in self.passageiro_normal:
                index = self.passageiro_normal.index(None)
                self.passageiro_normal[index] = passageiro
                self.vagas -= 1
                print(
                    f"Não há cadeiras preferenciais disponíveis. Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira normal {index}.")
                return True

    def descer(self, nome):
        if self.passageiro_prioritario.count(None) == 0:
            for i, passageiro in enumerate(self.passageiro_prioritario):
                if passageiro and passageiro.nome == nome:
                    self.passageiro_prioritario.remove(passageiro)
                    self.vagas += 1
                    print(f"Passageiro {nome} desceu da cadeira preferencial.")
                    return True
            return False
        elif self.psg_normal:
            for i, passageiro in enumerate(self.psg_normal):
                if passageiro and passageiro.nome == nome:
                    self.passageiro_normal.remove(passageiro)
                    self.vagas += 1
                    print(f"Passageiro {nome} desceu da cadeira normal.")
                    return True
            return False
        else:
            print(f"Passageiro {nome} não encontrado na topic.")
            return False

    def toString(self):
        return None