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
a.append(1000);		#inicializando o vetor da especie A
b.append(2000);		#inicializando o vetor da especie B
c.append(3000);		#inicializando o vetor da especie C
d.append(100);		#inicializando o vetor da especie D

lambdaA = 0.025		#taxa de crescimento da especie A
lambdaB = 0.030		#taxa de crescimento da especie B
lambdaC = 0.035		#taxa de crescimento da especie C
lambdaD = 0.005		#taxa de crescimento da especie D

alpha1 	= 0.0005		#taxa de decrescimento por predacao da especie A
alpha2 	= 0.0015		#taxa de decrescimento por poluicao da especie A 
beta1  	= 0.0008		#taxa de decrescimento por predacao da especie B 
beta2	= 0.0015		#taxa de decrescimento por poluicao da especie B 
gama1	= 0.0009		#taxa de decrescimento por predacao da especie C 
gama2	= 0.0015		#taxa de decrescimento por poluicao da especie C 

epsilon = 0.0012	#taxa de decaimento do poluente

K	= 10000		#Capacidade de suporte do meio

n	= 106		#tempo de simulacao em semanas (aproximadamente 53 semanas = 1 ano)
x	= 20		#semana em que ocorre o acidente

#print ("a ", a[0], "b ", b[0], "c ", c[0], "d ",d[0])

#Laco de tempo e a situacao de cada um dos individuos da dinamica e no instante n ocorre o acidente
for i in range(0,n):
	if i == x:
		a.append(a[i] - (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -alpha1*a[i]*d[i]))
		b.append(b[i] - (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -beta1*b[i]*d[i]))
		c.append(c[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -gama1*c[i]*d[i]))
		d.append(d[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + alpha1*a[i]*d[i] +beta1*b[i]*d[i]+ gama1*c[i]*d[i]))
		p.append(100.00);
	elif i > x:
		a.append(a[i] - (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -alpha1*a[i]*d[i]))
		b.append(b[i] - (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -beta1*b[i]*d[i]))
		c.append(c[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -gama1*c[i]*d[i]))
		d.append(d[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + alpha1*a[i]*d[i] +beta1*b[i]*d[i]+ gama1*c[i]*d[i]))
		p.append(p[i] - p[i]*epsilon);
	else:
		a.append(a[i] - (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -alpha1*a[i]*d[i] - alpha2*p[i]*a[i]))
		b.append(b[i] - (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -beta1*b[i]*d[i] - beta2*p[i]*b[i]))
		c.append(c[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) -gama1*c[i]*d[i] - gama2*p[i]*c[i]))
		d.append(d[i] - (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + alpha1*a[i]*d[i] +beta1*b[i]*d[i]+ gama1*c[i]*d[i]))
		p.append(p[i] + 0);
	print(a[i])

#Plotando o grafico
plt.plot(a, 'bo-');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

