import math

#função que calcula o valor Q
def getQ (max, min, n):
    return (max-min)/(math.pow(2,n)-1)


#função que converte uma cadeia de binários em um número real
def bin_dec(bin):
	res = 0
	for i in range(len(bin)-1,-1,-1):
		aux = float(bin[i])
		res = res + ((aux)*math.pow(2,(-i + len(bin) - 1)))
		i=i-1
	return res
