print("O que você quer executar?")
print("\n1-Operações")
print("\n2-Listas, Tuplas e Dicionários")
print("\n")














# operações
#SOMA
print(1+1)
#SUBTRAÇÃO
1-1-3
#MULTIPLICAÇÃO
4*4
#DIVISÃO 
4/4
#EXPONENCIAÇÃO
2 ** 2
#RESTO DA DIVISÃO 
3 % 4
#DIVISÃO DE CHÃO
3 // 4 
#PRIORIZAÇÃO 
(2 + 2) * 5
#diz que vai ser feito a multiplição primeiro, depois a adição.
#respeitando as mesmas regras na notação matemática.

#variaveis
Nome = "PYTHON HAHAHHAHA"
Nome = str("qualquer coisa") #no caso define que a variável vai ser armazenada como string.
inteiro = int(200)
flutuante = float(10.90)
booleano = bool(True)

'''#tipos de dados
    listas- criadas com colchetes []
    tuplas- criadas usando parenteses ()
    dicionários- criados usando chaves {}
'''
Lista_Exemplo_01 = [1,2,3,4,5]
Lista_Exemplo_02 = [ "Nome", "Sobrenome", "Idade", 4, 5]
Lista_Exemplo_03 = [1, "Texto", True, [1,2,3]]
print (Lista_Exemplo_03)

#tuplas são imutáveis!

Tupla_Exemplo_01 = (1,2,3,4)
Tupla_Exemplo_02 = ("texto", True, 2, 2.90)
print (Tupla_Exemplo_02)

#dicionários 

Dicionario_Exemplo_01 = {
    
    "Index": "Valor",
    "Id": 1,
    "Id": 2,
    "Nome": "Odemir"
}



'''
Nomeação de variáveis

'''
Laranja, Melao, Limao = 1,2,3
print( Laranja, Melao, Limao)
#essa declaração toda é válida. 

Morango = Uva = kiwi = 100
print (Morango, Uva, kiwi)

#nomear com listas
Lista_Carros= ['VW', 'Audi', 'Tesla']
Marca_01, Marca_02, Marca_03 = Lista_Carros
print(Marca_01, Marca_02, Marca_03)

#combinar variáveis
nome='Odemir'
sobrenome='depieri'

Nome_Completo= nome + sobrenome

print( Nome_Completo)



'''
Tipo de informação

1-text type : str
2-Numeric types: int, float, complex
3-Sequence types: list, tuple, range
4-Mapping type: dict
5-Set types: set, frozenset
6-boolean type: bool
7-binary type: bytes, bytearray, memoryview
'''

String = str('Ola Mundo')
Inteiro = int( 10 )
Fluante = float (100.5)
Complex = complex (1j)
Lista = list ( ('Maça', 'Morango') )
Tupla = tuple ( ('A', 'B') )
Range = range (6)
Dicionario = dict( nome='Odemir', age=29 )
Set = set (('A', 'B', 'C'))
Fronzet = frozenset( ('A', 'B', 'C'))
Boleano = bool(5)
Bytes = bytes (5)
ByteArray = bytearray (5)
MemoryView = memoryview (bytes(5))

'''from datatime import datetime
Data = datatime.today().date()
'''

'''
Comando Round
comando para arredondar valores de números flutuantes.
'''
Valor_Exemplo = 12.123456789
round(Valor_Exemplo, 2)


'''
Comando Len
função len() retorna a quantidade de elementos de qualquer lista em Python
'''
len(Lista_Exemplo_01)
len(Dicionario_Exemplo_01)
len(Tupla_Exemplo_01)
len(String)


'''
Fatiamento de Strings
'''


Minha_String = "Aprender Python é TOP!"

print (type (Minha_String))
print (len (Minha_String))

print(Minha_String[0])

print(Minha_String[11])

print(Minha_String[0:8])


'''
Manipulação de Strings
existem vários comandos, são os seguintes 

replace
startswith
endswith
count
capitalize
isdigit
isalnum
upper
lower
find
strip
split

'''


Minha_String.replace("TOP", "PAIA")
#Substitui o valor anterior da string por um novo
print("\n", Minha_String)

#Veririca o começo da string, com resultado boleano
Minha_String.startswith('Aprender')

#Verifica o fim da string, com resultado boleano
Minha_String.endswith('!')

#contar palavras/letras
print(Minha_String.count('P'))


#transformação nos textos
Nome1 = "pedro"

Nome1.capitalize()
#faz com que a primeira letra da string fica em maíusculo

#Vereficar se existe digitos na string
cpf="123456789"
print('\n\n', cpf);
print(cpf.isdigit(), '\n\n');

print(Minha_String)
print(Minha_String.isdigit(),'\n\n')


#verifica se a string é apenas alfanumérica
print('alnum')
print(Minha_String.isalnum(),'\n\n')


#deixa toda a string em maísculo
Minha_String = Minha_String.upper()
print(Minha_String,'\n')

#deixa toda a string em minúsculo
print(Minha_String.lower(),'\n')


#procura em qual posição uma palavra começa em uma string
frase = 'está calor hoje'
print(frase)
print(frase.find('calor'))
#caso a palavra não seja encontrada, retornará -1


#remove espaço livre no começo e no final da string
endereço= ' R Augusto 120, SP '
print(endereço)
print(endereço.strip())


#quebra a string
palavra = 'Rua Augusta 150, Centro, SP'
print(palavra.split(','))



'''
Comando Input, a função input() recebe como parâmetro uma string que 
será mostrada como auxílio ao usuário, geralmente o informando
que tipo de dado o programa está aguardando receber
'''

#Nome_input = input("Qual o seu nome: ")
#Idade_input = input("Qual a sua idade: ")

#print("Seu nome é:", Nome_input)
#print("Sua idade é:", Idade_input)



'''
Operadores de Comparação

1.'==' (Igual a)
2.'!=' (Diferente de)
3.'>' (maior)
4.'<' (menor)
5.'>=' (Maior igual)
6.'<=' (Menor igual)
'''

print(10 == 10)
print(10 == 8)
print(10 != 8)
print(10>8)
print(10<8)
print(10<=8)
print(10>=8)