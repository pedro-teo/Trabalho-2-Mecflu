## Trabalho 2 - Mecanica dos Fluidos
## Caio Brandao Krakauer - 11234287
## Murilo Ferreira Alves Batista - 11317060
## Pedro Henrique Teodoro Silva - 11805314
## Ricardo Chiquetto Do Lago - 4777623

#  Cabecalho
import math
import numpy as np
import matplotlib.pyplot as plt

# Declaracoes

## Nusps
nusp1 = [0,4,7,7,7,6,2,3]
nusp2 = [1,1,2,3,4,2,8,7]
nusp3 = [1,1,8,0,5,3,1,4]
nusp4 = [1,1,3,1,7,0,6,0]


## Variaveis
g = 9.8
D = 5/100
Cd = 0.47

## Inicio dos calculos
rhoSobreRhoS = 1.1 + 0.4*((nusp1[2]+nusp2[2]+nusp3[2]+nusp4[2])/4)
V0 = 3.0 + 0.1*((nusp1[3]+nusp2[3]+nusp3[3]+nusp4[3])/4)
alfa = -g*(rhoSobreRhoS - 1)
beta = (-3/4)*rhoSobreRhoS*Cd/D

h = (1/(2*beta))*math.log((alfa/beta)/(V0*V0 + alfa/beta))
T = (-1/(beta*math.sqrt(alfa/beta)))*math.atan(V0/math.sqrt(alfa/beta))

# calculo da velocidade em funcao de tempo
V = lambda t : math.sqrt(alfa/beta)*math.tan(beta*math.sqrt(alfa/beta)*t + math.atan(V0/math.sqrt(alfa/beta)))

# definicao do tempo
t = np.arange(0, 2*T, 0.01)

# criando vetor de posicao
posicao = np.zeros(len(t))

# definindo as posicoes ao longo do tempo
for i in range(0, len(t)-1):
    posicao[i] = (1/(2*beta))*math.log((V(t[i])*V(t[i]) + alfa/beta)/(V0*V0 + alfa/beta))

# plotando a figura
plt.figure(figsize = (12, 8))
plt.plot(t, posicao, 'b--', label='Solucao')
plt.axhline(y = h, color = 'r', linestyle = '-', label='Hmax')
plt.title('Profundidade da bolinha em funcao do tempo')
plt.xlabel('t')
plt.ylabel('z(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()