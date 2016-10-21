#!/usr/bin/python3

#Esse programa simula a poluicao de uma represa onde existe variacao na 
#quantidade de poluentes inserido por semana no sistema

# F = Fluxo de agua
# V = Volume de agua
# d = decaimento
# q = quantidade de poluente
# p[] = vetor temporal de quantidade de poluente
# n = numero de semanas

import matplotlib.pyplot as plt

F = 1
V = 100
d = 0.05
q = 5
p = []
n=100

l = (1-F/V -d);

p.append(0);

#Para entradas de uma quantidade q por semana
#for i in range(n):
#	p.append(p[i] * l + q);

#Para entradas: 0, 2q, 0, 2q...
#for i in range(n):
#	if i % 2 == 0:
#		p.append(p[i] * l + 2*q)
#	else:	
#		p.append(p[i] * l + 0)

#Para entradas: 0, 0, 3q, 0, 0, 3q...
for i in range(n):
	if i % 3 == 0:
		p.append(p[i] * l + 3*q)
	else:	
		p.append(p[i] * l + 0)

plt.plot(p, 'bo-');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

