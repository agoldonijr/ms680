#!/usr/bin/python3

import matplotlib.pyplot as plt


# b0, b1 e b2 sao valores iniciais para a brincadeira
#b0 = 5782
#b1 = 6812
#b2 = 8437
#n = Numero de anos
n = 50
# u = mortalidade (aproximadamente uma baleia vive 150 anos)
# y = 0.512 (percentual de filhotes)

u = 1/150
y = 0.512

#p = [] vetor de crescimento
b = []; 
b.append(5782)
b.append(6812)
b.append(8437)

i = 2;
#Para entradas de uma quantidade q por semana
for i in range(n):
       b.append(b[i] - u*b[i] + y*b[i-2]/2);

plt.plot(b, 'bo-');
plt.ylabel('Populacao');
plt.xlabel('Anos');
plt.show();


