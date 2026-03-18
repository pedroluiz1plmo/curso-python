import math
'''
1. Escreva um código que lê a lista abaixo e faça:

A leitura do tamanho da lista
A leitura do maior e menor valor
A soma dos valores da lista



lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
tam = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")
'''



'''
2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# Requisitando o número
num = int(input("Digite um número inteiro de 1 a 10:"))

# Gerando a função tabuada()
def tabuada(numero: int):
  print(f'Tabuada do {numero}:')
  for i in range(11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# lendo a tabuada do número escolhido
tabuada(num)
'''    


    
'''
3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:



# Lista gerada
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# declarando a lista de multiplos de 3 
mult_3 = []
# função para gerar uma lista dos múltiplos de 3 a partir de uma lista
def multiplo_3(lista: list) -> list:
  for i in range(len(lista)):
    # condição para um número ser múltiplo de 3
    if lista[i] % 3 == 0:
      mult_3.append(lista[i])
  return mult_3

# retornando a lista gerada para a variável mult_3
mult_3 = multiplo_3(lista)
mult_3
'''   




'''
4. Crie uma lista dos quadrados dos números da seguinte . 
Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_quadrados = []

lista_quadrados = map(lambda lista: pow(lista,2), lista)

print(list(lista_quadrados))
'''        
    
'''
5. Você foi contratado(a) como cientista de dados de uma associação de skate. 
Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
você precisa criar um código que calcula a pontuação dos(as) atletas. 
Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, 
você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. 
Retorne a média para apresentar o texto:

"Nota da manobra: [media]"


print('programa de cálculo de nota')
lista = []
i=5
for i in range(1,6):
    nota = float(input(f'digite a {i}º nota    '))    
    lista.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a nota da(o) skatista
media = media(notas)
print(f"Nota da manobra: {round(media, 1)}") 
'''    
   
   
'''
7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante 
concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome.
As listas são:
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:
"Nome completo: Ana Silva"


     
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)
'''



'''
8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados 
sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a 
pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando 
os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o 
aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, 
o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do 
time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:


Copiar código
Provável texto exibido:

"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
pontos = 0

def calcula_pontos(marcados, sofridos):
  total_pontos = 0
  
  # Usamos o range para acessar o mesmo índice nas duas listas
  for i in range(len(marcados)):
      if marcados[i] > sofridos[i]:
          total_pontos += 3  # Vitória
      elif marcados[i] == sofridos[i]:
          total_pontos += 1  # Empate
      else:
          pass # Derrota (0 pontos)
          
  return total_pontos

pontos = calcula_pontos(gols_marcados, gols_sofridos)

print('a quantidade de pontos foi de ', pontos)
'''  

       
'''
9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, 
sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, 
sendo que o valor da gasolina é de 5 reais o litro.
O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 
crie três funções nas quais: 

a 1ª função calcule os gastos com hotel (gasto_hotel), 
a 2ª calcule os gastos com a gasolina (gasto_gasolina) e 
a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gasto

'''

lista_cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
lista_distancia = [850, 800, 300, 550]
lista_passeio = [200, 400, 250, 300]
gasto = float(0.0)


def diaria(dias): # a 1ª função calcule os gastos com hotel (gasto_hotel), 
  valor = dias * 150
  return  valor

def litros(escolha_cidade, cidade, km): # a 2ª calcule os gastos com a gasolina (gasto_gasolina) e 
  valor = 5*(km[escolha_cidade]/14)
  return  valor

def passeio(escolha_cidade, escolha_dias, diaria): # a 3ª os gastos com passeio e alimentação (gasto_passeio).
  valor = diaria[escolha_cidade] * escolha_dias
  return valor3
    
    
    
i = 1
print ('selecione para qual cidade você vai')
for i in range(len(lista_cidades)):
  print(i, "  ", lista_cidades[i])
escolha_cidade = int(input())
    
escolha_dias = int(input("quantos dias pretendem ficar?"))  

gasto = diaria(escolha_dias) + litros(escolha_cidade, lista_cidades,lista_distancia) + passeio(escolha_cidade, escolha_dias, lista_passeio)  

total_litros = litros(escolha_cidade, lista_cidades,lista_distancia)

print("Com base nos gastos definidos, uma viagem de",escolha_dias, "dias para", escolha_dias, "saindo de Recife custaria", gasto)