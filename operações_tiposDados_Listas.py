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


'''
Operadores Lógicos

1. and (faz duas comparaçõse e só retorna verdadeiro se ambas forem verdadeiras)
2. or (se uma das duas for verdadeiro, retorna verdadeira)
3. not (inverte o resultado, torna false em verdadeiro e vice-versa)
'''
print('\n\n', 10 == 10 and 10 < 20)
print( 10>20 or 10<8)
print( not 10>20 or 10<8)




'''
Operadores de Identidade


is (retorna TRUE se ambas as variáveis forem o mesmo objeto)
is not (retorna TRUE se ambas as variáveis não forem o mesmo objeto)
'''

print('\n\n', type(Minha_String) is type(Nome_Completo))
print(type(Minha_String) is not type(Nome_Completo))




'''
Operadores de Associação 

in (retorna TRUE se uma sequência com o valor especificado estiver presente no objeto)
not in (retorna TRUE se uma sequência com o valor especificado não estiver presente no objeto)
'''

Lista_Ações = ['Magalu', 'Via', 'Carrefour']

'Via' in Lista_Ações #devolve TRUE
'zz' in Lista_Ações #devolve FALSE

'Via' not in Lista_Ações #devolve FALSE
'zz' not in Lista_Ações #devolve TRUE


'''
Manipulando Listas

Comandos mais utilizados:

    1- append() - Para adicionar um item ao final da lista 
    2- len() - Calcular o tamanho da lista
    3- [] - Acessar posições da lista
    4- del() - Excluir um elemento
    5- clear() - Limpar a lista
    6- insert() - Para inserir um item de lista em um índice específicado, empurrando os valores seguintes para a 'direita'
    7- extend() - Anexar elementos de outra lista à lista atual
    8- remove() - Remove o item especificado
    9- pop() - Remove o índice especificado
    10- sort() - Ordenar os avloers
    11-copy() - Faz uma cópia da lista
    12- index() - Retorna o index do elemento da lista
'''

Lista_Vazia = []
print ( Lista_Vazia )

Lista_Vazia.append( 1 )
Lista_Vazia.append( 2 )
Lista_Vazia.append( 3 )
Lista_Vazia.append( 'Valor' )

print ( Lista_Vazia )
print (Lista_Vazia[0])
print(len(Lista_Vazia))
#del(Lista_Vazia) vai apagar a lista e não vai mais ser possível acessá-la 
Lista_Vazia.clear()
print(Lista_Vazia)


Lista_Vazia.append( 1 )
Lista_Vazia.append( 2 )
Lista_Vazia.insert(0, '0')
print(Lista_Vazia)

Lista_01 = [1,2,3]
Lista_02 = [4,5,6]
Lista_01.extend(Lista_02)
print(Lista_01)

Lista_01.remove(5) #apaga o elemento em específico de uma lista, caso seja conhecido
Lista_01

Lista_01.pop(0) #apaga o lugar na lista, o que a gente chama de index
print(Lista_01)

Lista_ABC = ['z', 'c', 'f', 'H', 'A']
Lista_ABC.sort() #ordena a lista, em letras maísculas, e depois minúsculas, tudo em ordem alfabética.
print(Lista_ABC)

Lista_Nova = Lista_ABC

Lista_Nova.index('H') #retorna a posição do caractere procurado.


