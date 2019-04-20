#EP1_IA.py modificado para gerar arquivo texto
import math
import random
import datetime

from Populacao import Populacao
from Grafico import Grafico

# parâmetros iniciais
populacao = 200
geracoes = 100000
prob_mutacao = 0.1
prob_crossover = 0.7

# para o gráfico no relatório
melhores = []
media = []

#inicia população
p = Populacao(populacao, prob_mutacao, prob_crossover)
p.iniciaPopulacao()
i = 0

#nome de arquivo
nomeArq = 'arquivo01.txt'
print(datetime.datetime.now())

# gera arquivo de texto com dados de melhores / media
with open(nomeArq, 'w+') as f:
    # grava parametros no arquivo de texto
    f.write("Populacao: " + str(populacao) + " Geracoes: " + str(geracoes) + " Prob.Mutacao: " +
            str(prob_mutacao) + " Prob.Cross.: " + str(prob_crossover) + "\n")
    while (i < geracoes):
        print("geracao: " + str(i))
        # guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
        best = p.getMelhorIndividuo(melhores)
        p.insere_media(media)
        f.write(str(i) + ',' + "{:10.5f}".format(melhores[i]) + ',' + "{:10.5f}".format(media[i]) + ','
                + "{:10.5f}".format(math.fabs(melhores[i] - media[i])) + '\n')
        p.GA(melhores, media, populacao)
        # f.write(str(i) + ',' + "{:10.5f}".format(melhores[i]) + ',' + "{:10.5f}".format(media[i]) + ','
        #         + "{:10.5f}".format(math.fabs(melhores[i] - media[i])) + '\n')
        i = i + 1
f.close()

print('Terminou de criar txt!\t' + nomeArq)

print( datetime.datetime.now() )

# p.imprime()

# instancia grafico e imprime
graf = Grafico(populacao, prob_mutacao, prob_crossover, nomeArq)
graf.imprime()
