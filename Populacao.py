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

    def getMelhorIndividuo(self, melhores):
        aux = -1000
        index_melhor = 0
        for i in range(self.no_individuos):
            if(self.individuos[i].fitnessInverso > aux):
                aux = self.individuos[i].fitnessInverso
                index_melhor = i
        melhores.append(self.individuos[index_melhor].fitness)
        return index_melhor

    def getMedia(self):
        somaFitness = 0
        for i in range(self.no_individuos):
            somaFitness = somaFitness + self.individuos[i].fitness
        media = somaFitness / self.no_individuos
        return media

    def insere_media(self, media):
        media.append(self.getMedia())

    def GA(self, melhores, media, populacao):    
        novaPopulacao = []

        # crossover
        while(len(novaPopulacao) < populacao):
            mascara = Individuo.random_genome(self.bits_x + self.bits_y)
            filho1 = []
            filho2 = []
            index_pai1 = self.roleta()
            pai1 = self.individuos[index_pai1]
            index_pai2 = self.roleta()
            pai2 = self.individuos[index_pai2]

            cross = random.uniform(0,1)
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

            # mutação
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
            ind1 = Individuo(self.bits_x, self.min_x, self.max_x, self.bits_y, self.min_y, self.max_y)
            ind1.setCromossomoPronto(filho1)
            ind2 = Individuo(self.bits_x, self.min_x, self.max_x, self.bits_y, self.min_y, self.max_y)
            ind2.setCromossomoPronto(filho2)

            novaPopulacao.append(ind1)
            novaPopulacao.append(ind2)

        self.individuos.clear()
        self.individuos = novaPopulacao
