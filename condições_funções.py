import time


'''
Arquivo que irá abordar laços, condições, funções.


Docstring for condições_funções
'''

'''
1. Condição IF


'''

Idade = 18

if Idade >= 18 :
    print("você é maior de idade")

elif Idade >=15 and Idade <=17: #pode usar o or também.
    print("Seu pai ou mãe pode autorizar!!")

else:
    print("você não é maior de idade")



'''
2. Laço FOR


'''
#trabalhando Range
for QualquerCoisa in range(3):
    print(QualquerCoisa)

for QualquerCoisa in range(2,11):
    print(QualquerCoisa)

print('\n')

for QualquerCoisa in range(2,11, 2):
    print(QualquerCoisa)

Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']

for QualquerCoisa in Lista: #o for aqui vai percorrer toda a lista
    print(QualquerCoisa.upper()[0:3])

for Pais in Lista:
    if Pais == 'Uruguai':
        print(Pais, 'é Bi campeão da copa do mundo!!')
    
    for AlgumaCoisa in range(3):
        print(AlgumaCoisa)

for Loop in range (len(Lista)):
    print(Lista[Loop])
    
Lista[2]

for Loop in range(0, len(Lista), 2):
    print(Lista[Loop])

for Loop in range(3):
    print('\n')



#dá de fazer assim ou
for Index, Pais in enumerate(Lista):
    print(Index,Pais)


#duas maneiras de fazer a mesma coisa
x=0
#assim
for Pais in Lista:
    print(x, Pais)
    x+= 1



#criar lista enumarada a partir de um range
#o que é bem rápido.
[ Numero for Numero in range(0,10,2) ]
#gerando os valor 0, 2, 4, 6, 8, 10 na lista.


[ Numero == 2 for Numero in range(0,10,2) ]
#aqui os valores vão estar ao quadrado


#outra maneira de se fazer é
Lista = []
for Loop in range(0,10):
    Lista.append(Loop)

print(Lista)




'''
3- Estrutura de Loop WHILE

Loop que só para quando uma condição determinada
for alcançada
'''
for Loop in range(3):
    print('\n')

Parar = 0

while Parar <= 5:
    print(Parar)
    Parar+= 1


Loop = 0

import random

while Loop<=10:
    print(Loop)

    if Loop == 5:
        for x in range(10):
            print(random.random())
    
    Loop+=1



for Loop in range(3):
    print('\n')

#JOGUINHO pra explicar o uso de break em loop infinito
while True:
    Eu = random.randint(0, 10)
    Eles= random.randint(0, 10)

    print(Eu, Eles)
    if Eu > Eles:
        print('Tudo nosso nada deles!!!')
        break

    else:
        print('Um dia vai ser tudo nosso...')
        break

for Loop in range(3):
    print('\n')



'''
4- BREAK e CONTINUE

break é utilizado para parar um loop abruptamente
enquanto o continue é usado para ignorar algo e continuar um loop
'''

Lista = ['Morango', 'Pera', 'Uva', 'Abacaxi']

for Fruta in Lista:
    print(Fruta)

    if Fruta == 'Uva':
        break



for Loop in range(3):
    print('\n')


for Loop in range(0,11):
    if Loop ==5:
        continue #vai ignorar o if, apesar de verificar a condição
        print('Cheguei aqui mas vou ser ignorado!')
    
    print(Loop)

for Loop in range(3):
    print('\n')

'''
5-Estrutura de Funções
tu já sabe o que é, graças a deus chegou
'''

def Boas_Vindas():
    print('******* PYTHON *******')

Boas_Vindas()


#Soma
def Somar(Valor_1, Valor_2):
    Soma= Valor_1 + Valor_2
    print(Soma)

x=1
y=3
Somar(x,y)

for Loop in range(3):
    print('\n')

for Loop in range(0,10):
    import random

    x = random.random()
    y = random.random()
    Somar(x, y)


for Loop in range(3):
    print('\n')

'''
6-Estrutura Lambda

é uma função anônima
recebe qualquer número de argumento, mas apenas uma expressão

'''
Funcao_Soma = lambda valor: valor + 10

print(Funcao_Soma(1))


Funcao_Soma_02 = lambda valor_1, valor_2 : valor_1 + valor_2
print(Funcao_Soma_02(10,10))



'''
7-Estrutura TRY

permite que teste um bloco de código, mitigando um erro

O try permite testar um bloco de código quanto a erros.
O except permite que você lide com o erro.
O else permite executar código quando não há erro.
O finally permite que você execute código, independentemente do resultado dos blocos try e except

'''

try:
    0/0 #como a divisão é impossível, ele vai pro except
    print('Deu certo meu script!!')

except:
    print('Não deu certo')

finally:
    print('Vou ser executado da mesma forma!!!')

for Loop in range(3):
    print('\n')

'''
8-Estrutura de Classes/Objetos

Python é uma linguagem de programação orientaa a objetos.
Quase tudo em Python é um objeto, com suas propriedades e métodos.
Uma classe é como um construtor de objetos, ou um 'projeto' para criar objetos.
'''

class Pessoa:

    # Método Construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade
    

    def Boas_Vindas(self):
        print('Olá, seja bem vindo: ', self.Nome)


    def Recusado(self):
        print("seu acesso foi recusado!")

    # Função
    def Maior_Idade(self):
        if self.Idade >= 18:
            print('Usuário é maior de idade')
            self.Boas_Vindas()
        else:
            print('Usuário é menor de idade')
            self.Recusado()

Dados = Pessoa('Odemir', 29)
Dados.Maior_Idade()

for Loop in range(2):
    print('\n')


Dados_1 = Pessoa('Luiz', 12)
Dados_1.Maior_Idade()


'''
9-Módulos/Pacotes

Considere um módulo como sendo o mesmo que uma biblioteca de códigos
Para instalar um pacote utilize o 'pip install'
'''



'''
10-prints formatados
'''


print('Soma de 2+2 é:', 2+2)
print(f'Soma de 2+2 é: {2+2}')
print('Soma de 2+2 é: {}'.format(2+2) )