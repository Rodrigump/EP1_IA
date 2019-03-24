import math
import random

from Populacao import Populacao

# parâmetros iniciais
populacao = 10
geracoes = 1000000


# para o gráfico no relatório
melhores = []
media = []




# sample code
p = Populacao(populacao)
p.iniciaPopulacao()
i = 0
while(i < geracoes):
    p.GA(melhores, media, populacao)
    print(i, '\t', melhores[i], '\t', media[i],
          '\t', math.fabs(melhores[i] - media[i]))
    i = i + 1
