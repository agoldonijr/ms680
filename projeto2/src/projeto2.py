#!/usr/bin/python3

#############################################################################################################
#Para a utilizacao desse programa, eh necessario a instalacao do python3 e da biblioteca python3-matplotlib
#
#Para Debian/Ubuntu
#sudo apt-get install python3 python3-matplotlib
#
#Para Red-Hat/CentOS
#sudo yum install --enablerepo=epel python3 python3-matplotlib
#
#Verifica a documentacao junto a https://www.python.org/downloads/windows/ para instalacao no Windows
#
#Para a executar o programa, em um terminal, digite: 
#python3 projeto2.py
#
#Esse programa foi desenvolvido por Alcides Goldoni Junior - Bacharel Matematica Aplicada e computacional - 
#Unicamp e pode ser utilizado por qualquer pessoa, desde que cite em suas referencias.
#############################################################################################################

############################################################################################################
#O programa abaixa simula a dinamica populacional entre 4 especies de peixes, onde 3 delas disputam o meio
# e a quarta eh um predador comum das outras 3 especies.
#Em um dado periodo, eh despejado um quantidade de poluente no meio, afetando negativamente as especies 
#predadas e nao afetando a especie predadora.
#
#Todos as variaveis e estao descritas logo abaixo
###########################################################################################################

#importa da biblioteca que cria os graficos
import matplotlib.pyplot as plt

#Inicializacao das variaveis
p 	= []			#Vetor que contará a quantidade de poluicao
a 	= []			#Vetor que conterá os indiviuos da especie A
b 	= []			#Vetor que conterá os indiviuos da especie B
c 	= []			#Vetor que conterá os indiviuos da especie C
d 	= []			#Vetor que conterá os indiviuos da especie D
total	= []

p.append(0);			#inicializando o vetor de poluicao
a.append(30000);		#inicializando o vetor da especie A
b.append(20000);		#inicializando o vetor da especie B
c.append(10000);		#inicializando o vetor da especie C
d.append(1000);			#inicializando o vetor da especie D
total.append(61000)		#total de individuos

lambdaA = 0.024			#taxa de crescimento da especie A
lambdaB = 0.026			#taxa de crescimento da especie B
lambdaC = 0.028			#taxa de crescimento da especie C
lambdaD = 0.01			#taxa de crescimento da especie D

alpha1 	= 0.00000005		#taxa de decrescimento por predacao da especie A
alpha2 	= 0.00054		#taxa de decrescimento por poluicao da especie A 
beta1  	= 0.00000008		#taxa de decrescimento por predacao da especie B 
beta2	= 0.00056		#taxa de decrescimento por poluicao da especie B 
gama1	= 0.00000009		#taxa de decrescimento por predacao da especie C 
gama2	= 0.00058		#taxa de decrescimento por poluicao da especie C 

zeta	= 0.004			#taxa de descrescimento do predador por morte natural

mi 	= 0.00000002		#taxa de crescimento do predador enquanto tem presa

epsilon = 0.05			#taxa de decaimento do poluente

K	= 100000		#Capacidade de suporte do meio

n	= 106			#tempo de simulacao em semanas (aproximadamente 53 semanas = 1 ano)
x	= 25			#semana em que ocorre o acidente


#Laco de tempo e a situacao de cada um dos individuos da dinamica e no instante n ocorre o acidente
for i in range(0,n):
	#ocorrecia do acidente
	if i == x:
		a.append(a[i] + (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - alpha1*a[i]*d[i]))
		b.append(b[i] + (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - beta1*b[i]*d[i]))
		c.append(c[i] + (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - gama1*c[i]*d[i]))
		d.append(d[i] + (lambdaD *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + mi*a[i]*d[i] +mi*b[i]*d[i]+ mi*c[i]*d[i] ))
		p.append(100);
		total.append(a[i]+b[i]+c[i]+d[i])
		print ("Poluente entrou")
	
	#a partir daqui o acidente aconteceu temos poluicao na agua
	elif i > x:
		a.append(a[i] + (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - alpha1*a[i]*d[i] - alpha2*p[i]*a[i]))
		b.append(b[i] + (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - beta1*b[i]*d[i] - beta2*p[i]*b[i]))
		c.append(c[i] + (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - gama1*c[i]*d[i] - gama2*p[i]*c[i]))
		d.append(d[i] + (lambdaD *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + mi*a[i]*d[i] +mi*b[i]*d[i]+ mi*c[i]*d[i] ))
		p.append(p[i] - p[i]*epsilon);
		total.append(a[i]+b[i]+c[i]+d[i])
	
	#o acidente ainda nao occoreu
	else:	
		a.append(a[i] + (lambdaA *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - alpha1*a[i]*d[i]))
		b.append(b[i] + (lambdaB *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - beta1*b[i]*d[i]))
		c.append(c[i] + (lambdaC *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) - gama1*c[i]*d[i]))
		d.append(d[i] + (lambdaD *(a[i] + b[i] + c[i] +d[i])*( 1 - (a[i] + b[i] + c[i] +d[i])/K) + mi*a[i]*d[i] + mi*b[i]*d[i]+ mi*c[i]*d[i] ))
		p.append(p[i] + 0);
		total.append(a[i]+b[i]+c[i]+d[i])
	print(i, a[i])

############################################################################################################
#Para o plot dos graficos, comente com # as linhas que nao deseja plotar 
############################################################################################################
#Plotando o grafico
plt.plot(a, 'bo-');
plt.plot(b, 'go-');
plt.plot(c, 'yo-');
plt.plot(d, 'ro-');
plt.plot(total, 'ko-')
#plt.plot(p, 'ko-')
plt.ylabel('Número de indivíduos');
plt.xlabel('Semana');
plt.show();

