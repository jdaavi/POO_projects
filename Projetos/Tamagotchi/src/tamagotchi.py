class Tamagotchi:
    def __init__(self,energia ,saciedade,limpeza,idade):
        self.energia = energia
        self.energia_maxima = energia
        self.saciedade = saciedade
        self.saciedade_maxima = saciedade
        self.limpeza = limpeza
        self.limpeza_maxima = limpeza
        self.idade = 0
        self.idade_maxima = idade
        self.diamantes = 0
        self.vivo = True


    def getEnergiaMax(self):
       return self.energia_maxima 

    def getEnergiaAtual(self):
        return self.energia  

    def getSaciedadeMax(self):
        return self.saciedade_maxima

    def getSaciedadeAtual(self):
        return self.saciedade 
    
    def getLimpezaMax(self):
        return self.limpeza_maxima
    
    def getLimpezaAtual(self):
        return self.limpeza
    
    def getIdadeMax(self):
        return self.idade_maxima
    
    def getIdadeAtual(self):
        return self.idade
    
    def getDiamantes(self):
        return self.diamantes
    
    def getEstaVivo(self):
        return self.status()

    def status(self):
        if self.energia == 0 or self.saciedade == 0:
            self.vivo = False
            print("Seu bichinho morreu")

        else:
            print("O Status do seu bichinho está vivo:")
            print(f'energia : {self.energia}')
            print(f'saciedade : {self.saciedade}')
            print(f'limpeza : {self.limpeza}')
            print(f'idade : {self.idade}')
            print(f'ele possui: {self.diamantes} diamantes')


    def brincar(self):
            self.energia -= 2
            self.saciedade -= 1
            self.limpeza -= 3
            self.diamantes += 1
            self.idade += 1
            self.status()


    def comer(self):
        self.energia -= 1
        self.saciedade += 4
        self.limpeza -= 2
        self.idade += 1
        self.status()

    def dormir(self):
        if self.energia <= (self.energia_maxima - 5):
         self.energia = self.energia_maxima
         self.saciedade -= 2
         self.idade += 1
         self.status()

    def banhar(self):
        self.energia -= 3
        self.saciedade -= 1
        self.limpeza = self.limpeza_maxima
        self.idade += 2
        self.status()



    



