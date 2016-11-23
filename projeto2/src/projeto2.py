#!/usr/bin/python3

#importa da biblioteca que cria os graficos
import matplotlib.pyplot as plt

#Inicializacao das variaveis
p = []			#Vetor que contará a quantidade de poluicao
a = []			#Vetor que conterá os indiviuos da especie A
b = []			#Vetor que conterá os indiviuos da especie B
c = []			#Vetor que conterá os indiviuos da especie C
d = []			#Vetor que conterá os indiviuos da especie D

p.append(0);		#inicializando o vetor de poluicao
a.append(0);		#inicializando o vetor da especie A
b.append(0);		#inicializando o vetor da especie B
c.append(0);		#inicializando o vetor da especie C
d.append(0);		#inicializando o vetor da especie D

lambdaA = 0.25		#taxa de crescimento da especie A
lambdaB = 0.25		#taxa de crescimento da especie B
lambdaC = 0.25		#taxa de crescimento da especie C
lambdaD = 0.08		#taxa de crescimento da especie D

alpha1 	= 0.05		#taxa de decrescimento por predacao da especie A
alpha2 	= 0.15		#taxa de decrescimento por poluicao da especie A 
beta1  	= 0.05		#taxa de decrescimento por predacao da especie B 
beta2	= 0.15		#taxa de decrescimento por poluicao da especie B 
gama1	= 0.05		#taxa de decrescimento por predacao da especie C 
gama2	= 0.15		#taxa de decrescimento por poluicao da especie C 

epsilon = 0.03		#taxa de decaimento do poluente

K	= 10000		#Capacidade de suporte do meio

n	= 106		#tempo de simulacao em semanas (aproximadamente 53 semanas = 1 ano)
x	= 20		#semana em que ocorre o acidente


for i in range(n):
	if i == x:
		p.append(100.00);
	if i > x:
		a.append(lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -alpha1*a[i]*d[i]);
		b.append(lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -beta1*b[i]*d[i]);
		c.append(lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -gama1*c[i]*d[i]);
		d.append(lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + alpha1*a[i]*d[i] +beta1*b[i]*d[i]+ gama1*c[i]*d[i]);
		p.append(p[i] - p[i]*epsilon);
		print (i, p[i]);
	else:
		a.append(lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -alpha1*a[i]*d[i] - alpha2*p[i]*a[i]);
		b.append(lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -beta1*b[i]*d[i] - beta2*p[i]*b[i]);
		c.append(lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -gama1*c[i]*d[i] - gama2*p[i]*c[i]);
		d.append(lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + alpha1*a[i]*d[i] +beta1*b[i]*d[i]+ gama1*c[i]*d[i]);
		p.append(p[i] + 0);

#Plotando o grafico
plt.plot(p, 'bo-');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

