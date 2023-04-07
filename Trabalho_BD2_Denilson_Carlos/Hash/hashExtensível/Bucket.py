#from __future__ import annotations

class Bucket:#classe dos buckets

    def __init__(self, tam_bucket, pLocal): ## construtor 
        self.tamBucket = tam_bucket
        self.pLocal = pLocal
        self.val = []    #lista de valores do bucket
        
    def get_size(self): ## pega o tamanho da lista de valores.
        return len(self.val)

    def get_profLocal(self):  ## retorna a profundidade local
        return self.pLocal

    def set_profLocal(self, profLocal):  ##acessores 
        self.pLocal = profLocal
    
    def set_val(self, val):    ##acessores 
        self.val = val

    def is_empty(self):  # retorna verdadeiro ou falso 
        return len(self.val) == 0

    def is_full(self):   ## retorna se o bucket está cheio
        return len(self.val) == self.tamBucket - 1



    
