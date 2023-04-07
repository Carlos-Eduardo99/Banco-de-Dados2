#import math
from math import pow

class Diretorio:
    def __init__(self, pGlobal):  ### Construtor.
        self.pGlobal = pGlobal
        self.tamDiretorio = int(pow(2, pGlobal))  # Tamanho do diretório.
        #print('Tamanho do diretório é',self.tamDiretorio)
        self.EndBuckets = []                      # Endereços de buckets indexados no diretório.
        
        for cont in range(self.tamDiretorio):
            self.EndBuckets.append(cont)
        print(self.EndBuckets)  # Mostra o tamanho do diretório
    
    def funcaoHash(self, chave) -> int: ## Apenas diz que a função retorna um inteiro. 
        #print("função Hash",chave % pow(2, self.pGlobal))
        return int(chave) % int (pow(2, self.pGlobal))
    
    def retornaEnd(self, chave) -> int:
        return self.EndBuckets[self.funcaoHash(chave)]
    
    #Atualiza a profundidade global, e adiciona a lista de endereços os novos endereços espelhados

    def duplicarDiretorio(self):
        self.pGlobal += 1   #incremento
        for cont in range (int(pow(2, self.pGlobal)/2)): # Dobra o diretório.
            self.EndBuckets.append(self.EndBuckets[cont]) # adiciona ao diretorio, no final da lista os novos endereços
        print("O tamanho do diretorio agora é:",len(self.EndBuckets))

    #realoca os endereços um sim e um não a cada valor igual ao endereço inicial

    def realocarEnderecos(self, endIni, novoEnd): # endIni é endereco inicial
        # O novo endereço pro novo bucket
        #print('endIni ', endIni , 'novoEnd0',novoEnd)
        
        troquei = True
        for cont in range (len(self.EndBuckets)):
            if(self.EndBuckets[cont] == endIni):
                if(not troquei):  #se troquei for falso 
                    self.EndBuckets[cont] = novoEnd
                    troquei = True
                else:
                    troquei = False
    
    