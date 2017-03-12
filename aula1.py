#!/bin/python3

#Esse programa simula a poluição de uma represa
#
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

p.append(0);
#n = 60
n = 90

for i in range(n):
        p.append(p[i] * (1-F/V -d) + q);

#print (p);

plt.plot(p, 'bo')
plt.ylabel('Poluição');
plt.xlabel('Semana');

plt.show();
