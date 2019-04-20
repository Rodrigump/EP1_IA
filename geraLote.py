# gera arquivos em lotes
# testar em EP1_IA_mod pra ter noção do tempo depois configurar aqui para gerar vários
import math
import random
import datetime

from Populacao import Populacao
from Grafico import Grafico

# parâmetros iniciais
populacao = 200
geracoes = 1000
prob_mutacao = 0.01
prob_crossover = 0.7

#loop de arquivos:
for i in range(1, 6):

    # para o gráfico no relatório
    melhores = []
    media = []

    #inicia população
    p = Populacao(populacao, prob_mutacao, prob_crossover)
    p.iniciaPopulacao()
    # i = 0

    #nome de arquivo
    nomeArq = 'arquivo' + str(i) + '.txt'
    print("Gerando lote de arquivos...")
    print(datetime.datetime.now())

    # gera arquivo de texto com dados de melhores / media
    j = 0
    with open(nomeArq, 'w+') as f:
        # grava parametros no arquivo de texto
        f.write("Roleta+Roleta(original)   Populacao: " + str(populacao) + " Geracoes: " + str(geracoes) + " Prob.Mutacao: " +
                str(prob_mutacao) + " Prob.Cross.: " + str(prob_crossover) + "\n")
        while (j < geracoes):
            # guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
            best = p.getMelhorIndividuo(melhores)
            p.insere_media(media)

            p.GA(melhores, media, populacao)
            f.write(str(j) + ',' + "{:10.5f}".format(melhores[j]) + ',' + "{:10.5f}".format(media[j]) + ','
                    + "{:10.5f}".format(math.fabs(melhores[j] - media[j])) + '\n')
            j = j + 1
    f.close()

    print('Terminou de criar txt!\t' + nomeArq)
    print(datetime.datetime.now())

print("Finalizado arquivos em lote.")
