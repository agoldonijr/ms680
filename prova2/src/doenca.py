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
#python3 doenca.py
#
#Esse programa foi desenvolvido por Alcides Goldoni Junior - Bacharel Matematica Aplicada e computacional - 
#Unicamp e pode ser utilizado por qualquer pessoa, desde que cite em suas referencias.
#############################################################################################################


#############################################################################################################
#Essa programa faz a simulacao de uma doenca com caracteristicas parecidas com a gripe. Levando em consideracao o modelo SIRS incluindo ou nao uma taxa de vacinacao.
#############################################################################################################

# Biblioteca para plotar os graficos
import matplotlib.pyplot as plt

#vetor de quantidade de individuos
S = []		#Suscetiveis
R = []		#Resistentes
I = []		#infectados
r = []		#removidos

#inicializacao da quantidade de individuos
S.append(1000)
I.append(50)
R.append(10)
r.append(0)

alpha	= 0.030		#crescimento suscetivel
beta	= 0.030		#crescimento infectados
gamma	= 0.030		#crescimento dos resistente

phi	= 0.0065		#resistente -> suscetiveis
epsilon	= 0.031		#infectados -> removidos
laMbda	= 0.0000035		#suscetiveis -> infectados
omega	= 0.0063		#infectados -> resistentes

delta	= 0.005	#vacinacao

T=150

#O volume do rio eh constante, a retirada ou a insercao de agua no rio faz ele apenas diminuir ou aumentar a velocidade da agua

#sem vacina
#for i in range(0,T):
#	S.append( S[i] + alpha * S[i] - laMbda * S[i]*I[i] + phi * R[i]) ;
#	I.append( I[i] + beta * I[i] +  laMbda * S[i]*I[i] - omega * I[i] - epsilon * I[i]);
#	R.append( R[i] + gamma * R[i] + omega * I[i] - phi * R[i]);
#	r.append( r[i] + epsilon * r[i] );

#com vacina 
for i in range(0,T):
	S.append( S[i] + alpha * S[i] - laMbda * S[i]*I[i] + phi * R[i] - delta * S[i]) ;
	I.append( I[i] + beta * I[i] +  laMbda * S[i]*I[i] - omega * I[i] - epsilon * I[i]);
	R.append( R[i] + gamma * R[i] + omega * I[i] - phi * R[i] + delta * S[i]);
	r.append( r[i] + epsilon * r[i] );

plt.plot(S, 'bo-', label='Suscetivel');
plt.plot(R, 'ro-', label='Resistente');
plt.plot(I, 'go-', label='Infectado');
plt.plot(r, 'yo-', label='Removido');
plt.legend(loc='upper left');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

