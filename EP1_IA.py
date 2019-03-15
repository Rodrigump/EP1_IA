import math
import random

#valores hipoteticos (baseado no exemplo visto em aula)
bits_x1 = 10
min_x1 = -2
max_x1 = 3

bits_x2 = 10
min_x2 = 0
max_x2 = 4

def f(x1,x2): #funcao hipotetica de fitness
	return ((x1-2)**2) + ((x2-3)**2)

#função que calcula o valor de q, dado max, min e número de bits
def getQ (max, min, n):
    return (max-min)/((2**n)-1)

#função que calcula o número de bits necessários, dado max, min e q
def getN (max, min, q):
	return math.floor(math.log(((max-min)/q)+1) / math.log(2))

#função que converte uma cadeia de binários em um número real
def bin_dec (cadeia, inicio, fim):
	res = 0
	aux = 0
	for i in range(fim,inicio-1,-1):
		res = res + (cadeia[i]*(2**aux))
		aux = aux + 1
	return res
#Função para gerar o genoma (vetor binário) aleatório
def random_genome(size):
    return [random.randrange(0, 2) for _ in range(0, size)]

#Assumindo que genoma 1 e 2 são do mesmo tamanho
def cross_over(first_genome,second_genome):
    cross_over_point = random.randint(0,(len(first_genome)))
    for pos in range(0,cross_over_point):
        temp = first_genome[pos]
        first_genome[pos] = second_genome[pos]
        second_genome[pos] = temp
	
class Individuo:

    def __init__ (self): #Construtor da classe
        self.no_genes = bits_x1 + bits_x2 #tamanho da cadeia
        self.genotipo = random_genome(self.no_genes) #cadeia de bits
        self.x1_real = min_x1 + (getQ(max_x1,min_x1,bits_x1) * bin_dec(self.genotipo, 0, bits_x1-1))
        self.x2_real = min_x2 + (getQ(max_x2,min_x2,bits_x2) * bin_dec(self.genotipo, bits_x1, (bits_x1 + bits_x2)-1))
        self.fitness = f(self.x1_real,self.x2_real) #aplica o valor do fenotipo a funcao de fitness

    def imprime (self): #imprime a cadeia de bits
        for i in range(self.no_genes):
            print(self.genotipo[i],end="",flush=True)
        print('\t',self.fitness)
            
class Populacao:

    def __init__ (self,  no_individuos): #Construtor da classes
        self.no_individuos = no_individuos #numero de individuos da populacao
        self.individuos = [] #arranjo de individuos
        for i in range(no_individuos):
            self.individuos.append(Individuo())

    def imprime(self): #imprime o genotipo de todos os individuos da populacao
        for i in range(self.no_individuos):
            self.individuos[i].imprime()

    def roleta (self): #retorna o indice do individuo escolhido na roleta
        somaPesos = 0
        for i in range (self.no_individuos):
            somaPesos = somaPesos + self.individuos[i].fitness

        valor = somaPesos * random.uniform(0,1)
        for i in range(self.no_individuos):
            valor = valor - self.individuos[i].fitness
            if(valor < 0):
                return i
        return self.no_individuos - 1	

#sample code
p = Populacao(10)
p.imprime() #vai imprimir a cadeia de bits e o fitness de todos os individuos
