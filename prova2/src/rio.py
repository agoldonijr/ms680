#!/usr/bin/python3

#Esse programa simula a poluicao de uma represa onde existe variacao na 
#quantidade de poluentes inserido por semana no sistema

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
fluxoSetor1 = 1
fluxoSetor2 = 0.9
fluxoSetor3 = 0.95
fluxoSetor4 = 1.1
fluxoSetor5 = 0.87
fluxoSetor6 = 0.91
fluxoSetor7 = 1.20

#quantidade do fluxo que o afluente aumenta o fluxo
afluente1 = 0.3
afluente2 = 0.4
afluente3 = 0.11
afluente4 = 0.21
afluente5 = 0.17
afluente6 = 0.09
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
fonteSetor1 = 5
fonteSetor2 = 6
fonteSetor3 = 2
fonteSetor4 = 9
fonteSetor5 = 3
fonteSetor6 = 1
fonteSetor7 = 10

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

T=100

#O volume do rio eh constante, a retirada ou a insercao de agua no rio faz ele apenas diminuir ou aumentar a velocidade da agua
VOLUME = 100

#l = (1-F/V -d);


#
for i in range(0,T):
	pSetor1.append( pSetor1[i] * (1 - fluxoSetor1 / VOLUME - decSetor1  - atAgricola1) + fonteSetor1 + afluente1);
	pSetor2.append( pSetor2[i] * (1 - pSetor1[i] * fluxoSetor2 / VOLUME - decSetor2  - atAgricola2) + fonteSetor2 + afluente2);
	pSetor4.append( pSetor3[i] * (1 - pSetor2[i] * fluxoSetor3 / VOLUME - decSetor3  - atAgricola3) + fonteSetor3 + afluente3);
	pSetor3.append( pSetor4[i] * (1 - pSetor3[i] * fluxoSetor4 / VOLUME - decSetor4  - atAgricola4) + fonteSetor4 + afluente4);
	pSetor5.append( pSetor5[i] * (1 - pSetor4[i] * fluxoSetor5 / VOLUME - decSetor5  - atAgricola5) + fonteSetor5 + afluente5);
	pSetor6.append( pSetor6[i] * (1 - pSetor5[i] * fluxoSetor6 / VOLUME - decSetor6  - atAgricola6) + fonteSetor6 + afluente6);
	pSetor7.append( pSetor7[i] * (1 - pSetor6[i] * fluxoSetor7 / VOLUME - decSetor7  - atAgricola7) + fonteSetor7 + afluente7);


plt.plot(pSetor1, 'bo-');
plt.plot(pSetor2, 'ro-');
plt.plot(pSetor3, 'go-');
plt.plot(pSetor4, 'yo-');
plt.plot(pSetor5, 'co-');
plt.plot(pSetor6, 'mo-');
plt.plot(pSetor7, 'ko-');
plt.ylabel('Poluicao');
plt.xlabel('Semana');
plt.show();

