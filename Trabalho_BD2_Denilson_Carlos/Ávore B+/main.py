# -*- coding: utf-8 -*-
"""
Created on Mon Mar 7 15:40:10 2022

@author: Carlos e Denilson
"""

import time
from ArvoreBplus import Arvore_B_mais

if __name__=='__main__':
    
    cond = -1
    print('======= ÁRVORE B+ =======')
    while True:
        ordem = int(input('Digite a ordem da árvore b+: '))
        if ordem <= 2:
            print('Valor fora do esperado. A ordem tem que ser maior do que 2')
        else:
            break
    print('=========================')
    arvore = Arvore_B_mais(ordem) 

    arq = open('teste.csv','r')    # abre o arquivo em modo de leitura 'r'
    entr = []
    chaves = []
    valores = []                      # cria uma lista 
    print('Inserindo os valores do arquivo gerado!')
    inicio = time.time()               # medindo o tempo de execução 
    for linha in arq:                  # Lê cada linha do arquivo
        val = linha.split(',')     # A lista valores recebe cada elemento que está separado por virgula.
        if(val[0] == '+'):         # '+' Para valores que serão inseridos
            entr = list(map(int, val[1:]))     # Adiciona a lista de entrada cada valor inteiro 
            valores.append(entr[1:])    
            chaves.append(entr[0])     
    

                                            # map(aplica a função de inteiro em cada elemento)
                                            # Para visualizar os valores de entrada do arquivo linha por linha .
    for cont in chaves:
        arvore.inserir(chaves[cont], valores[cont])     # Chamada para inserção i = chave mostrar = false.

            #elif(val[0] == '-'):    # '-' para valores que serão excluidos.
            #    chave = int(val[1])
            #    arvore.remover(chave,False)
            
    fim = time.time()
    print('Tempo de execução: ',fim - inicio,' milissegundos')

    
    while(cond != 0):
        print(' 1 - Inserir \n 2 - Remover \n 3 - Buscar \n 4 - mostrar \n 0 - sair\n')

        opcao = int(input('Informe sua opção: '))

        if opcao == 1: ### Inserir
            aux = []
            cont = 1
            quant = int(input('Digite a quantidade de atributos: '))
            for cont in range(quant):
                aux.append(int(input('Digite os valores que deseja inserir: ')))
            chave = int(input('Digite a chave: '))
            inicio = time.time()
            arvore.inserir(chave, aux) ## Chamando o inserir. numero desejado para inserir e mostra que foi inserido.
            fim = time.time()
            print('Tempo de execução: ',(fim - inicio),' milissegundos')

        elif opcao == 2: ## Remover

            aux = []
            cont = 1
            quant = int(input('Digite a quantidade de atributos: '))
            for cont in range(quant):
                aux.append(int(input('Digite os valores que deseja excluir: ')))
            
            chave = int(input('Digite a chave para exclusão: '))
            inicio = time.time()
            arvore.deletar(chave, aux)   ## Chamando o deletar. numero desejado para remover e mostra que foi removido.
            fim = time.time()
            arvore.mostrar()
            print('Tempo de execução: ',fim - inicio,' milissegundos')


        elif opcao == 3: ### Buscar
            
            chave = (input('Digite a chave de busca: '))
            inicio = time.time()
             ## Chamando o buscar. numero desejado para buscar e mostra o numero buscado.
            if(arvore.buscar(chave)):
                print("Encontrado!")
            else:
                print("Não encontrado")
            fim = time.time()
            print('Tempo de execução: ',fim - inicio,' milissegundos')
        
        elif opcao == 4:
            arvore.mostrar()

        elif opcao == 0:     
            print('Saindo!')
            cond = 0

        elif opcao != 1 or 2 or 3 or 4 or 0 : ###and opcao != 2 and opcao != 3 and opcao != 0 and opcao != 4:
            print('Valor diferente do esperado!\n')