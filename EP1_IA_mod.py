#EP1_IA.py modificado para gerar arquivo texto
import math
import random
import datetime

from Populacao import Populacao
from Grafico import Grafico

# parâmetros iniciais
populacao = 50
geracoes = 500000
prob_mutacao = 0.01
prob_crossover = 0.7

# para o gráfico no relatório
melhores = []
media = []

# sample code
p = Populacao(populacao, prob_mutacao, prob_crossover)
p.iniciaPopulacao()
i = 0

nomeArq = 'arquivo01.txt'

print(datetime.datetime.now())

with open(nomeArq,'w+') as f:
    while(i < geracoes):
        #guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
        best = p.getMelhorIndividuo(melhores)
        p.insere_media(media)
        p.GA(melhores, media, populacao)
        f.write(str(i) + ',' + "{:10.2f}".format(melhores[i]) + ',' + "{:10.2f}".format(media[i]) + ',' 
                + "{:10.2f}".format(math.fabs(melhores[i] - media[i])) + '\n')
        i = i + 1
f.close()

print('Terminou de criar txt!\t' + nomeArq)

print( datetime.datetime.now() )

# instancia grafico e imprime
graf = Grafico(populacao, prob_mutacao, prob_crossover, nomeArq)
graf.imprime()
