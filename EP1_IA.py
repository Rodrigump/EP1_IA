import math
import random

from Populacao import Populacao

# parâmetros iniciais
populacao = 50
geracoes = 1000000
prob_mutacao = 0.01
prob_crossover = 0.7

# para o gráfico no relatório
melhores = []
media = []

# sample code
p = Populacao(populacao, prob_mutacao, prob_crossover)
p.iniciaPopulacao()
i = 0
while(i < geracoes):
    # guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
    best = p.getMelhorIndividuo(melhores)
    p.insere_media(media)
    p.GA(melhores, media, populacao)
    print(i, '\t', melhores[i], '\t', media[i],
          '\t', math.fabs(melhores[i] - media[i]))
    i = i + 1
