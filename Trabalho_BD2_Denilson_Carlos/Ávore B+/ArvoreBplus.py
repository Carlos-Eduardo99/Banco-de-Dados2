# -*- coding: utf-8 -*-
"""
Created on Mon Mar 7 15:40:10 2022

@author: Carlos e Denilson
"""

from math import ceil
from No import No

# Classe da árvore b+
class Arvore_B_mais:
    def __init__(self, ordem):
        self.raiz = No(ordem)
        self.raiz.verificar_folha = True

    # Operação de Inserção
    def inserir(self, chave, valor):
        chave = str(chave)
        no_antigo = self.procurar(chave)
        no_antigo.inserir_na_folha(no_antigo, chave, valor)

        if (len(no_antigo.chaves) == no_antigo.ordem):#Se a folha estiver cheia, insira a chave no nó folha em ordem crescente e balanceie a árvore 
            no1 = No(no_antigo.ordem)
            no1.verificar_folha = True 
            no1.pai = no_antigo.pai
            mid = int(ceil(no_antigo.ordem / 2)) - 1 #Cada nó pode conter no máximo m - 1 chaves e um mínimo de ⌈m/2⌉ - 1 chaves.
            no1.chaves = no_antigo.chaves[mid + 1:]
            no1.valores = no_antigo.valores[mid + 1:]
            no1.proxima_chave = no_antigo.proxima_chave
            no_antigo.chaves = no_antigo.chaves[:mid + 1]
            no_antigo.valores = no_antigo.valores[:mid + 1]
            no_antigo.proxima_chave = no1
            self.inserir_no_pai(no_antigo, no1.chaves[0], no1) #Adicionar m/2º chave para o nó pai também.

     # Inserir no pai
    def inserir_no_pai(self, n, chave, ndash):
         if (self.raiz == n):
             noRaiz = No(n.ordem)
             noRaiz.chaves = [chave]
             noRaiz.valores = [n, ndash]
             self.raiz = noRaiz
             n.pai = noRaiz
             ndash.pai = noRaiz
             return
    
         noPai = n.pai
         temp3 = noPai.valores
         for i in range(len(temp3)):
             if (temp3[i] == n):
                 noPai.chaves = noPai.chaves[:i] + \
                     [chave] + noPai.chaves[i:]
                 noPai.valores = noPai.valores[:i +
                                                   1] + [ndash] + noPai.valores[i + 1:]
                 if (len(noPai.valores) > noPai.ordem):
                     paiDash = No(noPai.ordem)
                     paiDash.pai = noPai.pai
                     mid = int(ceil(noPai.ordem / 2)) - 1 #Cada nó pode conter no máximo m - 1chaves e um mínimo de ⌈m/2⌉ - 1 chaves.
                     paiDash.chaves = noPai.chaves[mid + 1:]
                     paiDash.valores = noPai.valores[mid + 1:]
                     chave_ = noPai.chaves[mid]
                     if (mid == 0):
                         noPai.chaves = noPai.chaves[:mid + 1]
                     else:
                         noPai.chaves = noPai.chaves[:mid]
                     noPai.valores = noPai.valores[:mid + 1]
                     for j in noPai.valores:
                         j.pai = noPai
                     for j in paiDash.valores:
                         j.pai = paiDash
                     self.inserir_no_pai(noPai, chave_, paiDash)



    # Operação de busca utilizada em diferentes operações dentro da classe, Explora onde será inserido o nó
    def procurar(self, chave):
        noAtual = self.raiz
        while(noAtual.verificar_folha == False): #enquanto não chegou na folha
            temp2 = noAtual.chaves             #guardar o caminho
            for i in range(len(temp2)):
                if (chave == temp2[i]): #percorre o temp2
                    noAtual = noAtual.valores[i + 1] #se o chave for igual retorna o proximo nó
                    break
                elif (chave < temp2[i]):#se for menor retorna o nó atual
                    noAtual = noAtual.valores[i]
                    break
                elif (i + 1 == len(noAtual.chaves)):#se o indice + 1 for igual a quantidade de elementos
                    noAtual = noAtual.valores[i + 1]
                    break
        return noAtual #retorna o nó que devemos inserir

    # Encontra um nó
    def buscar(self, chave):
        l = self.procurar(chave)
        for i, item in enumerate(l.chaves):
            if l.chaves[i] == chave:
                print('Chave [',l.chaves[i],']','Valores: ',l.valores[i])
                return True
            else:
                return False

    # Deletar um nó
    def deletar(self, chave, valor):
        no_ = self.procurar(chave)

        temp = 0
        for i, item in enumerate(no_.chaves):
            if item == chave:
                temp = 1

                if valor in no_.valores[i]:
                    if len(no_.valores[i]) > 1:
                        no_.valores[i].pop(no_.valores[i].index(valor))
                    elif no_ == self.raiz:
                        no_.chaves.pop(i)
                        no_.valores.pop(i)
                    else:
                        no_.valores[i].pop(no_.valores[i].index(valor))
                        del no_.valores[i]
                        no_.chaves.pop(no_.chaves.index(chave))
                        self.deletarEntrada(no_, chave, valor)
                else:
                    print("Value not in Key")
                    return
        if temp == 0:
            print("Value not in Tree")
            return

    # Deletar uma entrada
    def deletarEntrada(self, no_, chave, valor):

        if not no_.verificar_folha:
            for i, item in enumerate(no_.valores):
                if item == valor:
                    no_.valores.pop(i)
                    break
            for i, item in enumerate(no_.chaves):
                if item == chave:
                    no_.chaves.pop(i)
                    break

        if self.raiz == no_ and len(no_.valores) == 1:
            self.raiz = no_.valores[0]
            no_.valores[0].pai = None
            del no_
            return
        elif (len(no_.valores) < int(ceil(no_.order / 2)) and no_.verificar_folha == False) or (len(no_.chaves) < int(ceil((no_.order - 1) / 2)) and no_.verificar_folha == True):

            is_predecessor = 0
            noPai = no_.pai
            noAnterior = -1
            proximoNo = -1
            PrevK = -1
            PostK = -1
            for i, item in enumerate(noPai.valores):

                if item == no_:
                    if i > 0:
                        noAnterior = noPai.valores[i - 1]
                        PrevK = noPai.chaves[i - 1]

                    if i < len(noPai.valores) - 1:
                        proximoNo = noPai.valores[i + 1]
                        PostK = noPai.chaves[i]

            if noAnterior == -1:
                ndash = proximoNo
                value_ = PostK
            elif proximoNo == -1:
                is_predecessor = 1
                ndash = noAnterior
                value_ = PrevK
            else:
                if len(no_.chaves) + len(proximoNo.chaves) < no_.order:
                    ndash = proximoNo
                    value_ = PostK
                else:
                    is_predecessor = 1
                    ndash = noAnterior
                    value_ = PrevK

            if len(no_.chaves) + len(ndash.chaves) < no_.order:
                if is_predecessor == 0:
                    no_, ndash = ndash, no_
                ndash.valores += no_.valores
                if not no_.verificar_folha:
                    ndash.chaves.append(value_)
                else:
                    ndash.nextKey = no_.nextKey
                ndash.chaves += no_.chaves

                if not ndash.verificar_folha:
                    for j in ndash.valores:
                        j.pai = ndash

                self.deletarEntrada(no_.pai, value_, no_)
                del no_
            else:
                if is_predecessor == 1:
                    if not no_.verificar_folha:
                        ndashpm = ndash.valores.pop(-1)
                        ndashkm_1 = ndash.chaves.pop(-1)
                        no_.valores = [ndashpm] + no_.valores
                        no_.chaves = [value_] + no_.chaves
                        noPai = no_.pai
                        for i, item in enumerate(noPai.chaves):
                            if item == value_:
                                noPai.chaves[i] = ndashkm_1
                                break
                    else:
                        ndashpm = ndash.valores.pop(-1)
                        ndashkm = ndash.chaves.pop(-1)
                        no_.valores = [ndashpm] + no_.valores
                        no_.chaves = [ndashkm] + no_.chaves
                        noPai = no_.pai
                        for i, item in enumerate(noPai.chaves):
                            if item == value_:
                                noPai.chaves[i] = ndashkm
                                break
                else:
                    if not no_.verificar_folha:
                        ndashp0 = ndash.valores.pop(0)
                        ndashk0 = ndash.chaves.pop(0)
                        no_.valores = no_.valores + [ndashp0]
                        no_.chaves = no_.chaves + [value_]
                        noPai = no_.pai
                        for i, item in enumerate(noPai.chaves):
                            if item == value_:
                                noPai.chaves[i] = ndashk0
                                break
                    else:
                        ndashp0 = ndash.valores.pop(0)
                        ndashk0 = ndash.chaves.pop(0)
                        no_.valores = no_.valores + [ndashp0]
                        no_.chaves = no_.chaves + [ndashk0]
                        noPai = no_.pai
                        for i, item in enumerate(noPai.chaves):
                            if item == value_:
                                noPai.chaves[i] = ndash.chaves[0]
                                break

                if not ndash.verificar_folha:
                    for j in ndash.valores:
                        j.pai = ndash
                if not no_.verificar_folha:
                    for j in no_.valores:
                        j.pai = no_
                if not noPai.verificar_folha:
                    for j in noPai.valores:
                        j.pai = noPai

    # função responsável por mostrar a árvore b+
    def mostrar(arvore):
        lst = [arvore.raiz] #pega o nó
        level = [0]
        leaf = None
        flag = 0
        lev_leaf = 0
    
        while (len(lst) != 0):#
            x = lst.pop(0)
            lev = level.pop(0)
            if (x.verificar_folha == False):
                for i, item in enumerate(x.valores):
                    print(item.chaves)
            else:
                for i, item in enumerate(x.valores):
                    print(item.chaves)
                if (flag == 0):
                    lev_leaf = lev
                    leaf = x
                    flag = 1