# só para visualização

from Grafico import Grafico

# parâmetros iniciais
populacao = 200
geracoes = 1000
prob_mutacao = 0.01
prob_crossover = 0.7

#arquivo a abrir
nomeArq = "arquivo1.txt"

# # 1 grafico
# graf = Grafico(populacao, prob_mutacao, prob_crossover, nomeArq)
# graf.imprime()

# grafico em lote
for i in range(1,6):
    #nome de arquivo
    nomeArq = 'arquivo' + str(i) + '.txt'

    graf = Grafico(populacao, prob_mutacao, prob_crossover, nomeArq)
    graf.imprime()