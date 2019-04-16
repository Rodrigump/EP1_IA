import math
import random


class Individuo:

    def __init__(self, bits_x, min_x, max_x, bits_y, min_y, max_y):  # Construtor da classe
        self.bits_x = bits_x
        self.min_x = min_x
        self.max_x = max_x
        
        self.bits_y = bits_y
        self.min_y = min_y
        self.max_y = max_y
        self.no_genes = self.bits_x + self.bits_y  # tamanho da cadeia

        self.fitness = 0
        self.fitnessInverso = 0

    # Função para gerar o genoma (vetor binário) aleatório
    @staticmethod
    def random_genome(size):
        return [random.randrange(0, 2) for _ in range(0, size)]

    # função que calcula o valor de q, dado max, min e número de bits
    @staticmethod
    def getQ(max, min, n):
        return (max - min) / ((2**n) - 1)

    # função que calcula o número de bits necessários, dado max, min e q
    @staticmethod
    def getN(max, min, q):
        return math.floor(math.log(((max - min) / q) + 1) / math.log(2))

    # função que converte uma cadeia de binários em um número real
    @staticmethod
    def bin_dec(cadeia, inicio, fim):
        res = 0
        aux = 0
        for i in range(fim, inicio - 1, -1):
            res = res + (cadeia[i] * (2**aux))
            aux = aux + 1
        return res

    def getFitness(self):  # funcao hipotetica de fitness
        pi = math.pi
        x_real = self.min_x + (self.getQ(self.max_x, self.min_x, self.bits_x)
                              * self.bin_dec(self.genotipo, 0, self.bits_x - 1))
        y_real = self.min_y + (self.getQ(self.max_y, self.min_y, self.bits_y)
                              * self.bin_dec(self.genotipo, self.bits_x, (self.bits_x + self.bits_y) - 1))
        return 20 + (x_real **2) + (y_real**2) - (10 * (math.cos(2 * pi * x_real) + math.cos(2 * pi * y_real)))

    def setCromossomoAleatorio(self):
        self.genotipo = self.random_genome(self.no_genes)  # cadeia de bits

        # aplica o valor do fenotipo a funcao de fitness
        self.fitness = self.getFitness()
        self.fitnessInverso = 1 / (self.fitness + (10**-9))

    def setCromossomoPronto(self, crom):
        self.genotipo = crom

        # aplica o valor do fenotipo a funcao de fitness
        self.fitness = self.getFitness()
        self.fitnessInverso = 1 / (self.fitness + (10**-9))

    def imprime(self):  # imprime a cadeia de bits
        letras = ""
        for i in range(self.no_genes):
            letras += str(self.genotipo[i])
            # print(self.genotipo[i], end="", flush=True)
        print(letras)
        print('\t', self.fitness)
