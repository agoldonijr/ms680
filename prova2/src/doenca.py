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
#python3 rio.py
#
#Esse programa foi desenvolvido por Alcides Goldoni Junior - Bacharel Matematica Aplicada e computacional - 
#Unicamp e pode ser utilizado por qualquer pessoa, desde que cite em suas referencias.
#############################################################################################################


#############################################################################################################


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
I.append(5)
R.append(0)
r.append(0)

alpha	= 0.03		#taxa de infeccao de sucetivel para infectado
beta	= 0.03		#
gama	= 0.03
phi	= 0.03
epsilon	= 0.03
laMbda	= 0.03
omega	= 0.03


T=20

#O volume do rio eh constante, a retirada ou a insercao de agua no rio faz ele apenas diminuir ou aumentar a velocidade da agua

#sem vacina
for i in range(0,T):
	s.append( s[i] - alpha * S[i] + laMbda * S[i] + phi * R[i]) ;
	I.append( I[i] + alpha * S[i] - beta * R[i] - gamma * r[i] + epsilon * I[i]);
	R.append( R[i] +  beta * R[i] + omega R[i] - phi * R[i]);
	r.append( r[i] + gamma * r[i] );
#com vacina 
#for i in range(0,T):
#	s.append( s[i] - alpha * S[i] + laMbda * S[i] + phi * R[i] - mi * S[i]) ;
#	I.append( I[i] + alpha * S[i] - beta * R[i] - gamma * r[i] + epsilon * I[i]);
#	R.append( R[i] +  beta * R[i] + omega R[i] - phi * R[i] + mi * S[i]);
#	r.append( r[i] + gamma * r[i] );


plt.plot(s, 'bo-', label='Suscetivel');
plt.plot(R, 'ro-', label='Resistente');
plt.plot(I, 'go-', label='Infectado');
plt.plot(r, 'yo-', label='Removido');
plt.legend(loc='upper left');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

