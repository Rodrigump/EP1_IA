import math
import random

#parâmetros iniciais
populacao = 10
prob_crossover = 0.7
prob_mutacao = 0.3

bits_x = 10
min_x = -5
max_x = 5
pi = math.pi

bits_y = 10
min_y = -5
max_y = 5

#para o gráfico no relatório
melhores = []
media = []

def insere_media ():
	soma = 0
	for i in range(len(melhores)):
		soma =  soma + melhores[i]
	media.append(soma / len(melhores))

def f(x,y): #funcao hipotetica de fitness
	return 20 + (x**2) + (y**2) - (10*(math.cos(2*pi*x)+math.cos(2*pi*y)))

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
		self.no_genes = bits_x + bits_y #tamanho da cadeia

	def setCromossomoAleatorio (self):
		self.genotipo = random_genome(self.no_genes) #cadeia de bits
		self.x_real = min_x + (getQ(max_x,min_x,bits_x) * bin_dec(self.genotipo, 0, bits_x-1))
		self.y_real = min_y + (getQ(max_y,min_y,bits_y) * bin_dec(self.genotipo, bits_x, (bits_x + bits_y)-1))
		self.fitness = f(self.x_real,self.y_real) #aplica o valor do fenotipo a funcao de fitness

	def setCromossomoPronto (self, crom):
		self.genotipo = crom
		self.x_real = min_x + (getQ(max_x,min_x,bits_x) * bin_dec(self.genotipo, 0, bits_x-1))
		self.y_real = min_y + (getQ(max_y,min_y,bits_y) * bin_dec(self.genotipo, bits_x, (bits_x + bits_y)-1))
		self.fitness = f(self.x_real,self.y_real) #aplica o valor do fenotipo a funcao de fitness

	def imprime (self): #imprime a cadeia de bits
		for i in range(self.no_genes):
			print(self.genotipo[i],end="",flush=True)
		print('\t',self.fitness)

class Populacao:

	def __init__ (self,  no_individuos): #Construtor da classes
		self.no_individuos = no_individuos #numero de individuos da populacao
		self.individuos = [] #arranjo de individuos
		self.prox = None #ponteiro para próxima população

	def iniciaPopulacao (self):
		for i in range(self.no_individuos):
			self.individuos.append(Individuo())
			self.individuos[i].setCromossomoAleatorio()

	def imprime(self): #imprime o genotipo de todos os individuos da populacao
		for i in range(self.no_individuos):
			self.individuos[i].imprime()

	def ajustaFitness(self):
		for i in range(self.no_individuos):
			self.individuos[i].fitness = 1 / (self.individuos[i].fitness + (10**(-9)))

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

	def getMelhorIndividuo(self):
		aux = -1
		index_melhor = 0
		for i in range(self.no_individuos):
			if(self.individuos[i].fitness > aux):
				aux = self.individuos[i].fitness
				index_melhor = i
		melhores.append(self.individuos[index_melhor].fitness)
		return index_melhor

	def GA (self):
		self.ajustaFitness()
		self.getMelhorIndividuo() #guarda o melhor indivíduo da geração atual no vetor estático 'melhores'
		insere_media()
		novaPopulacao = []

		#crossover
		while(len(novaPopulacao) < populacao):
			mascara = random_genome(bits_x + bits_y)
			filho1 = []
			filho2 = []
			index_pai1 = self.roleta()
			pai1 = self.individuos[index_pai1]
			index_pai2 = self.roleta()
			pai2 = self.individuos[index_pai2]

			for i in range(len(mascara)):
				if(mascara[i]==0):
					filho1.insert(i,pai1.genotipo[i])
					filho2.insert(i,pai2.genotipo[i])
				if(mascara[i]==1):
					filho1.insert(i,pai2.genotipo[i])
					filho2.insert(i,pai1.genotipo[i])

			#mutação
			for i in range(bits_x + bits_y):
				mutacao = random.uniform(0,1)
				if(mutacao < prob_mutacao):
					if(filho1[i]==0):
						filho1[i]=1
					else:
						if(filho1[i]==1):
							filho1[i]=0

			for i in range(bits_x + bits_y):
				mutacao = random.uniform(0,1)
				if(mutacao < prob_mutacao):
					if(filho2[i]==0):
						filho2[i]=1
					else:
						if(filho2[i]==1):
							filho2[i]=0
			ind1 = Individuo()
			ind1.setCromossomoPronto(filho1)
			ind2 = Individuo()
			ind2.setCromossomoPronto(filho2)

			novaPopulacao.append(ind1)
			novaPopulacao.append(ind2)

		self.individuos.clear()
		self.individuos = novaPopulacao

#sample code
p = Populacao(populacao)
p.iniciaPopulacao()
i = 1
lim = 10000
while(i<=lim):
	p.GA()
	i=i+1
print('Melhor da última geração\t',melhores[lim-1])
print('Média\t\t\t\t',media[lim-1])
