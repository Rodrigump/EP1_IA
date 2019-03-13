import math
import random

class Individuo:
    
    def __init__ (self, no_genes): #Construtor da classe
        self.no_genes = no_genes #tamanho da cadeia
        self.genotipo = random_genome(no_genes) #cadeia de bits
            
    def imprime (self): #imprime a cadeia de bits
        for i in range(self.no_genes):
            print(self.genotipo[i],end="",flush=True)
        print()
            
class Populacao:
    
    def __init__ (self, no_genes, no_individuos): #Construtor da classe
        self.no_genes = no_genes
        self.no_individuos = no_individuos #numero de individuos da populacao
        self.individuos = [] #arranjo de individuos
        for i in range(no_individuos):
            self.individuos.append(Individuo(no_genes))
    
    def imprime(self): #imprime o genotipo de todos os individuos da populacao
        for i in range(self.no_individuos):
            self.individuos[i].imprime()

#função que calcula o valor de q, dado max, min e número de bits
def getQ (max, min, n):
    return (max-min)/((2**n)-1)

#função que calcula o número de bits necessários, dado max, min e q
def getN (max, min, q):
	return math.floor(math.log(((max-min)/q)+1) / math.log(2))

#função que converte uma cadeia de binários em um número real
def bin_dec(bin):
	res = 0
	for i in range(len(bin)-1,-1,-1):
		aux = float(bin[i])
		res = res + ((aux)*(2**((-i + len(bin) - 1))))
		i=i-1
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

#sample code
first_genome = [0,0,0,0,0]
second_genome = [1,1,1,1,1]
print("Vetor A %s" % first_genome)
print("Vetor B %s" % second_genome)

cross_over(first_genome,second_genome)
print("Vetor A' %s" % first_genome)
print("Vetor B' %s" % second_genome)
