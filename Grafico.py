#Grafico.py
import matplotlib.pyplot as plt
import csv

class Grafico:
    
    def __init__(self,  no_individuos,  prob_mutacao, prob_crossover, nomeArq):  # Construtor da classes
        
        # parâmetros utilizados
        self.populacao = 99
        self.geracoes = 999999
        self.prob_mutacao = prob_mutacao
        self.prob_crossover = prob_crossover
        self.nomeArq = nomeArq       
    
    def imprime(self):
        # para o gráfico no relatório
        x = []
        y1 = []
        y2 = []
        # mudar tamanho do quadro de exibição
        fig = plt.figure(figsize=(15,6))
        
        print(self.nomeArq)
        print('Gerando gráfico...')
        with open(self.nomeArq,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            # lê linha de cabecalho
            rowHeader = next(plots)
            # utiliza linhas para gerar grafico
            for row in plots:
                x.append(int(row[0]))
                y1.append(float(row[1]))
                y2.append(float(row[2]))
        csvfile.close()
        #plt.ylim((0,5))

        plt.plot(x,y1, label='Melhores[1]'  , color = 'red'   ,linewidth=0.2)
        plt.plot(x,y2, label='Media[2]'     , color = 'green'    , linewidth=0.2)

        plt.xlabel('Gerações')
        plt.ylabel('Fitness')
        plt.title('pc = ' + str(self.prob_crossover) + ', pm = ' + str(self.prob_mutacao) )
        plt.legend()

        plt.show()
        print("Impressão de Grafico completa!")