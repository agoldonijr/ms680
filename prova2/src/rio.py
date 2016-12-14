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

#Esse programa simula a poluicao de uma represa com 7 setores, onde para cada setor existe uma quantidade de poluente inicial, a entrada de poluente do setor anterior, o decaimento do poluente naquele setor, a retirada de agua por atividade agricola e uma fonte de poluente por setor.

#############################################################################################################

# fluxoSetor*[]	= vetor temporal de quantidade de poluente em cada setor
# afluentes[]	= afluentes que desaguam nesse rio
# atAgricola[]	= retirada de agua pela atividade agricola
# decSetor[]	= decaimento em cada setor
# fonteSetor[]	= fonte de poluente por setor
# T 		= numero de semanas


# Biblioteca para plotar os graficos
import matplotlib.pyplot as plt

#criacao das variaveis e vetores

#fluxo de agua que entra em cada segmento do rio fluxoSetor1 = Fluxo que entrano setor 1 do rio
fluxoSetor1 = 0.9
fluxoSetor2 = 0.45
fluxoSetor3 = 0.95
fluxoSetor4 = 0.6
fluxoSetor5 = 0.87
fluxoSetor6 = 0.39
fluxoSetor7 = 0.77

#quantidade do fluxo que o afluente aumenta o fluxo
afluente1 = 0.3
afluente2 = 0.4
afluente3 = 0.31
afluente4 = 0.21
afluente5 = 0.27
afluente6 = 0.19
afluente7 = 0.2

#contidade do fluxo que a atividade agricula retira
atAgricola1 = 0.31
atAgricola2 = 0
atAgricola3 = 0.33
atAgricola4 = 0.18
atAgricola5 = 0.11
atAgricola6 = 0
atAgricola7 = 0.27

#valor do decaimento do poluente
decSetor1 = 0.05
decSetor2 = 0.06
decSetor3 = 0.1
decSetor4 = 0.08
decSetor5 = 0.09
decSetor6 = 0.044
decSetor7 = 0.03

#quantidade de poluente jogado no fluxo
fonteSetor1 = 0.5
fonteSetor2 = 0.6
fonteSetor3 = 0.2
fonteSetor4 = 0.9
fonteSetor5 = 0.3
fonteSetor6 = 0.1
fonteSetor7 = 0.9

#vetor de quantidade de poluicao
pSetor1 = []
pSetor2 = []
pSetor3 = []
pSetor4 = []
pSetor5 = []
pSetor6 = []
pSetor7 = []

#inicializacao de poluicao para cada setor do rio
pSetor1.append(5.0)
pSetor2.append(2.7)
pSetor3.append(3.1)
pSetor4.append(3.6)
pSetor5.append(3.0)
pSetor6.append(4.3)
pSetor7.append(9.3)

T=20

#O volume do rio eh constante, a retirada ou a insercao de agua no rio faz ele apenas diminuir ou aumentar a velocidade da agua
VOLUME = 10000

#l = (1-F/V -d);


#
for i in range(0,T):
	pSetor1.append( pSetor1[i] * (1 - fluxoSetor1 / VOLUME - decSetor1  - atAgricola1) + fonteSetor1 + afluente1);
	pSetor2.append( pSetor2[i] * (1 + pSetor1[i] * fluxoSetor2 / VOLUME - decSetor2  - atAgricola2) + fonteSetor2 + afluente2);
	pSetor4.append( pSetor3[i] * (1 + pSetor2[i] * fluxoSetor3 / VOLUME - decSetor3  - atAgricola3) + fonteSetor3 + afluente3);
	pSetor3.append( pSetor4[i] * (1 + pSetor3[i] * fluxoSetor4 / VOLUME - decSetor4  - atAgricola4) + fonteSetor4 + afluente4);
	pSetor5.append( pSetor5[i] * (1 + pSetor4[i] * fluxoSetor5 / VOLUME - decSetor5  - atAgricola5) + fonteSetor5 + afluente5);
	pSetor6.append( pSetor6[i] * (1 + pSetor5[i] * fluxoSetor6 / VOLUME - decSetor6  - atAgricola6) + fonteSetor6 + afluente6);
	pSetor7.append( pSetor7[i] * (1 + pSetor6[i] * fluxoSetor7 / VOLUME - decSetor7  - atAgricola7) + fonteSetor7 + afluente7);


plt.plot(pSetor1, 'bo-', label='Setor 1');
plt.plot(pSetor2, 'ro-', label='Setor 2');
plt.plot(pSetor3, 'go-', label='Setor 3');
plt.plot(pSetor4, 'yo-', label='Setor 4');
plt.plot(pSetor5, 'co-', label='Setor 5');
plt.plot(pSetor6, 'mo-', label='Setor 6');
plt.plot(pSetor7, 'ko-', label='Setor 7');
plt.legend(loc='upper left');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

