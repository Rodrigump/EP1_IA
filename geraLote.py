# gera arquivos em lotes
# testar em EP1_IA_mod pra ter noção do tempo depois configurar aqui para gerar vários
import math
import random
import datetime
import matplotlib.pyplot as plt

from Populacao import Populacao

# parâmetros iniciais
populacao = 10
geracoes = 1000000
prob_mutacao = 0.01
prob_crossover = 0.7

#loop de arquivos:
for i in range(0, 5):
    print("Arquivo: " + str(i) )
    # para o gráfico no relatório
    melhores = []
    media = []

    #inicia população
    p = Populacao(populacao, prob_mutacao, prob_crossover)
    p.individuos.clear()
    p.iniciaPopulacao()
    # i = 0

    #nome de arquivo
    nomeArq = 'arquivo' + str(i) + '.txt'
    print("Gerando lote de arquivos..." + str(datetime.datetime.now()) )

    # gera arquivo de texto com dados de melhores / media
    j = 0
    eixo_x = []
    melhorFitness = 100
    with open(nomeArq, 'w+') as f:
        # grava parametros no arquivo de texto
        f.write("Roleta+Roleta(original)   Populacao: " + str(populacao) + " Geracoes: " + str(geracoes) + " Prob.Mutacao: " +
                str(prob_mutacao) + " Prob.Cross.: " + str(prob_crossover) + "\n")
        while (j < geracoes):
            eixo_x.append(j)
            # guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
            best = p.getMelhorIndividuo(melhores)
            if p.individuos[best].fitness < melhorFitness:
                melhorFitness = p.individuos[best].fitness
            p.insere_media(media)

            p.GA(melhores, media, populacao)
            f.write(str(j) + ',' + "{:10.5f}".format(melhores[j]) + ',' + "{:10.5f}".format(media[j]) + ','
                    + "{:10.5f}".format(math.fabs(melhores[j] - media[j])) + '\n')

            # condição de parada
            if math.floor(media[j]*100)/100 == 0.00:
                print("Resposta encontrada!")
                break

            j = j + 1
        plt.plot(eixo_x, melhores, label='Melhor', color = 'red')
        plt.plot(eixo_x, media, label='Média', color = 'blue')
        plt.legend()
        plt.show()
    f.close()

    print('Terminou de criar txt!\t' + nomeArq + " " + str(datetime.datetime.now()) )

    print("Melhor Fitness: " + str(melhorFitness))

print("Finalizado arquivos em lote.")
