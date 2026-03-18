import datetime
import time
import math
import random
import statistics





'''
Pacote Externo - Datatime
import datetime
'''

Dia_Hoje = datetime.datetime.today()
print(Dia_Hoje)

Ano = Dia_Hoje.year
Mes = Dia_Hoje.month
Dia = Dia_Hoje.day

print(Ano, Mes, Dia)

Data = datetime.date(2021,1,24)
Data_Antiga = datetime.date(2022, 12, 24)
print(Data_Antiga)


print(Data_Antiga - Data) #comparação entre datas, dizendo quanto tempo se deu de uma pra outra.

Data.strftime('%d/%m/%y') #muda o formata da data, isto é, coloca ele no formato brasileiro de dia/mês/ano

print(Data + datetime.timedelta(days=30)) #soma mais 30 dias a variável selecionada


'''
Pacote Externo - Time 
import time
'''
print('comecei agora ...')
#time.sleep(2) espera por 2 segundos
print('Terminei')

Agora = time.localtime()
print(Agora,'\n',  type(Agora))

time.strftime('%m/%d/%y, %H:%M:%S', Agora)

Time_Texto = '21 June, 2021'
#time.strptime(Time_Texto, '%d %B, %Y') função que converte a data em texto para número.
print(time.strptime(Time_Texto, '%d %B, %Y'))



'''
Pacote Externo - Math
import math
'''
Tupla= (1, 4, 10 ,20 , 45)
Tupla_1 = (10,5,20,30,40)
min(Tupla) #seleciona o menor valor da tupla
max(Tupla_1) #seleciona o maior valor da tupla
abs(-7.25) #transforma o valor para positivo
pow(3, 4) #faz a potencição do primeiro número, elevado ao segundo número
math.sqrt( 81 ) #tira a raiz quadrada do número
math.ceil(1.4) #arredonda o número pra cima, até o número inteiro mais próximo
math.floor(1.4) #arredonda o número pra baixo, até o número inteiro mais próximo
math.pi #dá o valor de pi para algo



'''
Pacote Externo - Random

import random
gera números pseudo-aleatórios para várias distribuições
'''

Lista_aleatório = [1, 2, 3, 4, 5, 6, 7, 8]
random.choice(Lista_aleatório)

Palavra= 'Odemir'
random.choice(Palavra) #seleciona uma letra da palavra

random.random() #gera um valor aleatório entre 0 e 1

random.randint(0, 1000) #gera um valor aleatório inteiro, entre dois parâmetros definidos.



'''
Pacote Externo - Statistics

para calcular estatísticas matemáticas de dados numéricos e interage com as listas
'''

Lista_estas = [12, 15, 28, 56, 78, 80]

sum(Lista_estas) / len(Lista_estas) #fórmula para tirar a média de algo

statistics.mean( Lista_estas ) #função pronta para tirar a média de algo.
statistics.meadian (Lista_estas) #calcula a mediana dos valores
statistics.mode( Lista_estas ) #calcula a moda dos valores


