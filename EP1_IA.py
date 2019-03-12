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
def random_genoma(size):
    return [random.randrange(0, 2) for _ in range(0, size)]

#Convertendo o genoma em valor real
print(bin_dec(random_genoma(5)))
