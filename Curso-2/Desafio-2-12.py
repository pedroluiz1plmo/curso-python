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
'''
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]


def calcula_pontos(marcados, sofridos):
    pontos = 0

       

