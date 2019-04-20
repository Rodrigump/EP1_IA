import math
import random

from Individuo import Individuo

class Populacao:

    def __init__(self,  no_individuos,  prob_mutacao, prob_crossover):  # Construtor da classes
        self.prob_crossover = prob_crossover
        self.prob_mutacao =  prob_mutacao
        self.bits_x = 10
        self.min_x = -5
        self.max_x = 5

        self.bits_y = 10
        self.min_y = -5
        self.max_y = 5
        self.no_individuos = no_individuos  # numero de individuos da populacao
        self.individuos = []  # arranjo de individuos
        self.prox = None  # ponteiro para próxima população

    def iniciaPopulacao(self):
        for i in range(self.no_individuos):
            self.individuos.append(Individuo(self.bits_x, self.min_x, self.max_x, self.bits_y, self.min_y, self.max_y))
            self.individuos[i].setCromossomoAleatorio()

    def imprime(self):  # imprime o genotipo de todos os individuos da populacao
        for i in range(self.no_individuos):
            self.individuos[i].imprime()
        print("\t Media: " + str(self.getMedia()))
        print()

    def roleta(self):  # retorna o indice do individuo escolhido na roleta
        somaPesos = 0
        for i in range(self.no_individuos):
            somaPesos = somaPesos + self.individuos[i].fitnessInverso

        valor = somaPesos * random.uniform(0, 1)
        for i in range(self.no_individuos):
            valor = valor - self.individuos[i].fitnessInverso
            if(valor < 0):
                return i
        return self.no_individuos - 1

    def roletaTruncada(self):  # retorna o indice do individuo escolhido na roleta que elimina porcentagem dos piores
        somaPesos = 0
        percPop = int(self.no_individuos * 0.8)

        self.individuos.sort(key=lambda x: x.fitnessInverso)
        for i in range(percPop):
            somaPesos = somaPesos + self.individuos[i].fitnessInverso

        valor = somaPesos * random.uniform(0, 1)
        for i in range(percPop):
            valor = valor - self.individuos[i].fitnessInverso
            if(valor < 0):
                return i
        return self.no_individuos - 1

    def torneio(self):  # retorna indice de individuo escolhido por torneio
        arrInicio = []

        # gera 10 indices aleatórios
        while len(arrInicio) < 10:
            indiceRandom = random.randint(0, self.no_individuos-1)
            if indiceRandom not in arrInicio:
                    arrInicio.append(indiceRandom)

        # escolhe o que tiver maior fitness
        valFit = 1
        indice = 0
        for i in range(len(arrInicio)):
            # indice = 1
            # if self.individuos[arrInicio[i]].fitness > valFit :
            if self.individuos[arrInicio[i]].fitnessInverso < valFit:
                valFit = self.individuos[arrInicio[i]].fitnessInverso
                indice = arrInicio[i]

        return indice

    def getMelhorIndividuo(self, melhores):
        aux = -1000
        index_melhor = 0
        for i in range(self.no_individuos):
            if(self.individuos[i].fitnessInverso < aux):
                aux = self.individuos[i].fitnessInverso
            # if(self.individuos[i].fitness < aux):
            #     aux = self.individuos[i].fitness
                index_melhor = i
        melhores.append(self.individuos[index_melhor].fitnessInverso)
        # melhores.append(self.individuos[index_melhor].fitness)
        return index_melhor

    def getMedia(self):
        somaFitness = 0
        for i in range(self.no_individuos):
            # somaFitness = somaFitness + self.individuos[i].fitness
            somaFitness = somaFitness + self.individuos[i].fitnessInverso
        media = somaFitness / self.no_individuos
        return media

    def insere_media(self, media):
        media.append(self.getMedia())

    def GA(self, melhores, media, populacao):
        novaPopulacao = []

        # Elitismo - adiciona x% dos melhores
        elite = sorted(self.individuos, key=lambda x: x.fitnessInverso)
        for i in range(int(self.no_individuos*0.1)):
            novaPopulacao.append(elite[i])
        for i in range(5):
            print(str(novaPopulacao[i].fitness))
        while(len(novaPopulacao) < populacao):
            mascara = Individuo.random_genome(self.bits_x + self.bits_y)
            filho1 = []
            filho2 = []

            # Seleção =====================================================================================

            # seleção (roleta + roleta)
            index_pai1 = self.roleta()
            pai1 = self.individuos[index_pai1]
            index_pai2 = self.roleta()
            pai2 = self.individuos[index_pai2]

            # # seleção (roleta truncada)
            # index_pai1 = self.roletaTruncada()
            # pai1 = self.individuos[index_pai1]
            # index_pai2 = self.roletaTruncada()
            # pai2 = self.individuos[index_pai2]

            # # seleção (torneio + torneio)
            # index_pai1 = self.torneio()
            # pai1 = self.individuos[index_pai1]
            # index_pai2 = self.torneio()
            # pai2 = self.individuos[index_pai2]

            # # seleção (random)
            # index_pai1 = int(random.randrange(0, self.no_individuos))
            # pai1 = self.individuos[index_pai1]
            # index_pai2 = int(random.randrange(0, self.no_individuos))
            # pai2 = self.individuos[index_pai2]

            # # seleção (roleta + melhor)

            # index_pai1 = self.roleta()
            # pai1 = self.individuos[index_pai1]
            # index_pai2 = melhorIndice
            # pai2 = self.individuos[index_pai2]

            # selecao por rank
            # https://stackoverflow.com/questions/20290831/how-to-perform-rank-based-selection-in-a-genetic-algorithm
            # --

            #cross-over =========================================================================
            cross = random.uniform(0,1)

            #Cross-over: Uniforme(mascara)
            if(cross < self.prob_crossover):
                for i in range(len(mascara)):
                    if(mascara[i] == 0):
                        filho1.insert(i, pai1.genotipo[i])
                        filho2.insert(i, pai2.genotipo[i])
                    if(mascara[i] == 1):
                        filho1.insert(i, pai2.genotipo[i])
                        filho2.insert(i, pai1.genotipo[i])
            else: #se nao houver crossover, clona
                filho1 = pai1.genotipo
                filho2 = pai2.genotipo

            # #Cross-over: 1 ponto
            # if(cross < self.prob_crossover):
            #     corte = random.randint(0, 20)
            #     for p in range(0, self.bits_y + self.bits_y):
            #         if (p < 10):
            #             if corte < 9: # mantem gene do pai
            #                 filho1.insert(p, pai1.genotipo[p])
            #                 filho2.insert(p, pai2.genotipo[p])
            #             else:
            #                 filho1.insert(p, pai2.genotipo[p])
            #                 filho2.insert(p, pai1.genotipo[p])
            #         else:
            #             if p < corte:   # mantem gene do pai
            #                 filho1.insert(p, pai2.genotipo[p])
            #                 filho2.insert(p, pai1.genotipo[p])
            #             else:
            #                 filho1.insert(p, pai1.genotipo[p])
            #                 filho2.insert(p, pai2.genotipo[p])
            # else: #se nao houver crossover, clona
            #     filho1 = pai1.genotipo
            #     filho2 = pai2.genotipo

            # mutação =================================================================================================
            for i in range(self.bits_x + self.bits_y):
                mutacao = random.uniform(0, 1)
                if(mutacao < self.prob_mutacao):
                    if(filho1[i] == 0):
                        filho1[i] = 1
                    else:
                        if(filho1[i] == 1):
                            filho1[i] = 0
            for i in range(self.bits_x + self.bits_y):
                mutacao = random.uniform(0, 1)
                if(mutacao < self.prob_mutacao):
                    if(filho2[i] == 0):
                        filho2[i] = 1
                    else:
                        if(filho2[i] == 1):
                            filho2[i] = 0

            # monta cromossomos
            ind1 = Individuo(self.bits_x, self.min_x, self.max_x, self.bits_y, self.min_y, self.max_y)
            ind1.setCromossomoPronto(filho1)
            ind2 = Individuo(self.bits_x, self.min_x, self.max_x, self.bits_y, self.min_y, self.max_y)
            ind2.setCromossomoPronto(filho2)
            # inclui novos individuos
            novaPopulacao.append(ind1)
            novaPopulacao.append(ind2)

        self.individuos.clear()
        self.individuos = novaPopulacao
