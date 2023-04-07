# -*- coding: utf-8 -*-
"""
Created on Mon Mar 7 21:41:44 2022

@author: Carlos e Denilson
"""

import matplotlib.pyplot as plt 


# Input de tempo, dividido por ' ' (espaços)
yh = [float(x) for x in input("Inserir tempos de Hash (dividas por espaços): ").split()]
ya = [float(x) for x in input("Inserir tempos de Árvore B+ (dividas por espaços): ").split()]
x = [float(x) for x in input("Inserir intervalos (dividas por espaços): ").split()]

# Plotando pontos de Arvore B+
plt.plot(x, ya, label = "Árvore B+") 
# Plotando pontos de Hash
plt.plot(x, yh, label = "Hash") 
  
# Nomeando eixos
plt.xlabel('Intervalos')
plt.ylabel('Tempo de execução (s)') 

plt.legend() 

# Alterar nome a cada iteração
plt.savefig('exp.png', bbox_inches='tight')
  
plt.show() 

  