from Diretorio import Diretorio
from Bucket import Bucket
import sys

class hashextensivel:
    
    def __init__(self, pGlobal, tamBucket):      # Construtor
        self.tamBucket = tamBucket               # Quantidades de valores que um Bucket pode guardar 
        self.diretorio = Diretorio(pGlobal)      # Diretório que liga os buckets
        self.buckets = []
        ## se eu tiver um diretório de tamanho x vou criar x buckets
        for i in range(self.diretorio.tamDiretorio):    # Tamanho do diretório
            bucketAux = Bucket(self.tamBucket, pGlobal)  
            self.buckets.append(bucketAux)
            #print('O bucket tem tamanho',len(self.buckets)) ## Mostra o tamanho do bucket apenas para finalidades de teste..


    def inserir(self, chave, mostrar):
        indice = self.diretorio.retornaEnd(chave)  # Retorna o indice do bucket 
        ## print('vai inserir no: ',indice) Mostra em qual bucket vai inserir.
        cabe = self.buckets[indice].get_size() < self.tamBucket    #retorna um valor logico verdadeiro se oBucket não estiver cheio.
        if(cabe):
            self.buckets[indice].val.append(chave)   #insere o valor no bucket
            #caso caiba e a chave não exista no hash,ela é adicionada
            '''
            if chave not in self.buckets[indice].val:
                self.buckets[indice].val.append(chave)
                if(mostrar):
                    print("Valor inserido")
            else:
                if(mostrar):
                    print("valor já inserido")
            '''
        else:
            # Se o bucket estiver cheio e as profundidades forem iguais, duplicamos o diretório;
            # Atualizar as profundidades do bucket, e do diretorio;
            # Realocamos os endereços do bucket no diretório;
            # Redistribuir os valores e inserir a chave.


            pDiferentes = self.buckets[indice].pLocal != self.diretorio.pGlobal ## Profundidade diferentes = True.
            if(not pDiferentes):                                                ## Se as profundidades são igual 
                val = []
                self.diretorio.duplicarDiretorio()
                self.buckets[indice].pLocal += 1                          # Aumenta a profundidade local do bucket atual 
                aux = Bucket(self.tamBucket, self.buckets[indice].pLocal) # Cria um bucket auxiliar com a nova profundidade
                self.buckets.append(aux)                                  # adciona junto aos demais buckets
                self.diretorio.realocarEnderecos(indice, len(self.buckets) - 1)   #endereça o novo bucket
                for cont in range (len(self.buckets[indice].val)):
                    val.append(self.buckets[indice].val[cont]) #clona o bucket atual
                self.buckets[indice].val.clear()  #limpa o bucket atual 
                for valor in val: # Para cada valor no clone
                    self.inserir(valor,mostrar) # redestribuimos seus valores novamente nos buckets.
                val.clear()        
                self.inserir(chave,mostrar) #insere o valor atual
            else:
                #atualizar as profundidades do bucket
                #particionar o bucket , realocar os endereços do bucket no diretório
                #reinserir os valores e tentar inserir a chave
                val = []
                self.buckets[indice].pLocal += 1
                aux = Bucket(self.tamBucket, self.buckets[indice].pLocal)
                self.buckets.append(aux)
                self.diretorio.realocarEnderecos(indice, len(self.buckets) - 1)
                for cont in range (len(self.buckets[indice].val)):
                    val.append(self.buckets[indice].val[cont])
                self.buckets[indice].val.clear()
                for valor in val:
                    self.inserir(valor,mostrar)
                val.clear()
                self.inserir(chave,mostrar)
        
        
    def remover(self, chave,mostrar):
        try:
            indice = self.diretorio.retornaEnd(chave)
            self.buckets[indice].val.remove(chave)
            if(mostrar):
                print('Valor removido')
        except:
            if(mostrar):
                print('Não foi possivel remover o item informado')
        

    def mostrar(self):
        for buckets in self.buckets:
            print(buckets.val)
            
            
    def buscar(self, chave):
        indice = self.diretorio.retornaEnd(chave)
        if(chave in self.buckets[indice].val):
            print('Valor buscado foi encontrado! e é: {}'.format(chave))
            
        else:
            print('Valor não econtrado no Hash!!')        

    
def tamPagina(quantCampos, tamBytes):
    vet = [sys.maxsize] * quantCampos
    aux = quantCampos // sys.getsizeof(vet)
    print('O aux é: ',aux)
    return aux 