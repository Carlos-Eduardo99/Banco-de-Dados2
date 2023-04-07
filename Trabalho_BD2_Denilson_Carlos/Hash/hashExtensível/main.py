from Hash import hashextensivel ## importando o a classe hash do arquivo hash e renomeando com hashextensivel; 
import time ## biblioteca time para a medição do tempo de execução;

if __name__ == '__main__':      # escopo principal executa o que esta definido dentro da main.
   
    cond = '9'    ## variável de controle do while
    #profundidadeG = int(input('Informe a profundidade global: '))
    #tamBalde = int(input('Informe que quantidade de elementos deve ter no máximo cada bucket: '))

    #obj = hashextensivel(profundidadeG,tamBalde)  # criando um objeto da classe hashExtensível com a profundidade global e o tamanho do bucket 
    obj = hashextensivel(2,80)  # para usar as três linhas acima essa deve ser comentada
    
    arq = open('50000inserção.csv','r')    # abre o arquivo em modo de leitura 'r'
    entr = []                       # cria uma lista 
    print('Inserindo os valores do arquivo gerado!')
    inicio = time.time()               # medindo o tempo de execução 
    for linha in arq:                  # Lê cada linha do arquivo
        val = linha.split(',')     # A lista valores recebe cada elemento que está separado por virgula.
        if(val[0] == '+'):         # '+' Para valores que serão inseridos
            entr = list(map(int, val[1:]))     # Adiciona a lista de entrada cada valor inteiro 
                                               # map(aplica a função de inteiro em cada elemento)
            #print(entr)            # Para visualizar os valores de entrada do arquivo linha por linha .
            for elemento in entr:
                obj.inserir(elemento,True)     # Chamada para inserção i = chave mostrar = false.

        elif(val[0] == '-'):    # '-' para valores que serão excluidos.
            chave = int(val[1])
            obj.remover(chave,False)
            
    fim = time.time()
    print('Tempo de execução: ',fim - inicio,' milissegundos')

    
    while(cond != 0):
        print(' 1 - Inserir \n 2 - Remover \n 3 - Buscar \n 4 - mostrar \n 0 - sair\n')

        opcao = int(input('Informe sua opção: '))

        if opcao == 1: ### Inserir
            numero = int(input('Digite o valor que deseja inserir: '))
            inicio = time.time()
            obj.inserir(numero,True) ## Chamando o inserir. numero desejado para inserir e mostra que foi inserido.
            obj.mostrar()
            fim = time.time()
            print('Tempo de execução: ',(fim - inicio),' milissegundos')

        elif opcao == 2: ## Remover

            numero = int(input('Digite o valor que deseja remover: '))
            inicio = time.time()
            obj.remover(numero,True)  ## Chamando o remover. numero desejado para remover e mostra que foi removido.
            fim = time.time()
            obj.mostrar()
            print('Tempo de execução: ',fim - inicio,' milissegundos')


        elif opcao == 3: ### Buscar
            
            numero = int(input('Digite o valor que deseja buscar: '))
            inicio = time.time()
            obj.buscar(numero) ## Chamando o buscar. numero desejado para buscar e mostra o numero buscado.
            fim = time.time()
            obj.mostrar()
            print('Tempo de execução: ',fim - inicio,' milissegundos')
        
        elif opcao == 4:
            obj.mostrar()

        elif opcao == 0:     
            print('Saindo!')
            cond = 0

        elif opcao != 1 or 2 or 3 or 4 or 0 : ###and opcao != 2 and opcao != 3 and opcao != 0 and opcao != 4:
            print('Valor diferente do esperado!\n')
        
             