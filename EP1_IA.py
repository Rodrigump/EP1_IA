import math
import random

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
