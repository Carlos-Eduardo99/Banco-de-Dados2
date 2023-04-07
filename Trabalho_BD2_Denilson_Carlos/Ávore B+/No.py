# -*- coding: utf-8 -*-
"""
Created on Mon Mar 7 10:24:46 2022

@author: Carlos e Denilson
"""

"""Classe de Nó basica.
Cada nó carrega um par valor-chave, um status que indica se o nó é folha ou não e a sua ordem,
que é o número maximo de chaves que cada nó pode armazenar.
"""

class No:
    def __init__(self, ordem):          # Construtor
        self.ordem = ordem
        self.chaves = []
        self.valores = []
        self.proxima_chave = None
        self.pai = None
        self.verificar_folha = False

    # inserir na folha
    def inserir_na_folha(self, folha, chave, valor):
        if (self.chaves):
            temp1 = self.chaves
            for i in range(len(temp1)):
                if (chave == temp1[i]):
                    self.valores[i].append(valor)
                    break
                elif (chave < temp1[i]):
                    self.chaves = self.chaves[:i] + [chave] + self.chaves[i:]
                    self.valores = self.valores[:i] + [[valor]] + self.valores[i:]
                    break
                elif (i + 1 == len(temp1)):
                    self.chaves.append(chave)
                    self.valores.append(valor)
                    break
        else:
            self.chaves = [chave]
            self.valores = [valor]