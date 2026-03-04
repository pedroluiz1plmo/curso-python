import time



'''
texto = input('digite seu nome')
print('OLÁ',texto,', bem-vindo ao mundo do Python!')
'''

'''
print("calculadora de soma")
v1 = int(input('digite o primeiro valor'))
v2 = int(input('digite o segundo valor'))
print('soma:', v1 + v2)

'''


'''
print('conversor de medidas')
v1 = float(input('insira a medida em metros'))
escolha = int(input('pra qual medida você quer que seja feita \n1-cm \n2-mm\n'))
if escolha == 1 :
    v1 = v1 * 100
    print('a medida nova em centímetros é:',v1)
elif escolha == 2:
    v1 = v1 * 10000
    print('a medida nova em milímetro é:',v1)
else:
    print('escolha não válida!!')
'''


'''
print('calculo de média aritmética de nota de aluno\n')
n1 = float(input('digita a primeira nota'))
n2 = float(input('digite a segunda nota'))
n3 = float(input('digite a terceira nota'))
nm = (n1+n2+n3)/3
print('a média é de',nm)
'''

'''
print('conversor de temperatura\n ')
temperatura = float(input('digite a temperatura em Celsius:     '))
temperatura = temperatura * 1.8 + 32
print('a temperatura em fahrenheit', temperatura)
'''


'''
print(teste de par ou impar)
n = int(input('digite o número inteiro: '))
if n % 2 == 0:
    print(f"O número {n} é PAR.")
else:
    print(f"O número {n} é ÍMPAR.")
'''


'''
print('verificação de qual número é maior')
n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))

maior = max(n1, n2, n3) # A função max() já faz todo o trabalho!
print(f'O maior é {maior}')
'''



'''
print('radar de velocidade')
velocidade = int(input('digite a velocidade do carro'))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('ultrapassou a velocidade máxima, a multa é de:',multa)
else:
    print('dentro da velocidade permitida')
'''


'''
print('calculo de média aritmética de nota de aluno\n')
n1 = float(input('digita a primeira nota'))
n2 = float(input('digite a segunda nota'))
n3 = float(input('digite a terceira nota'))
nm = (n1+n2+n3)/3
print('a média é de',nm)
if nm >= 7:
    print('aprovado')
elif 5 < nm <= 6.9:
    print('Recuperação')
else:
    print('reprovado')
'''

'''
print('tabuada de um 1 a 10')
n= int(input('digite o número:'))
for Loop in range(1,11):
    print(n,'*',Loop,'=', n*Loop)
'''


'''
print("A contagem regressiva vai começar!")

# O range(início, fim, passo) funciona assim:
# 10: começa no 10
# -1: para antes de chegar ao -1 (ou seja, para no 0)
# -1: subtrai 1 a cada volta (o "passo")
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Faz o programa "dormir" por 1 segundo

print("💥 BUM! Feliz Ano Novo!")
'''
'''

ListaNomes = ['Pedro','Taise','Control','Malcom','Tood']
consulta = input("digite o nome a ser consultado")
for Loop in ListaNomes:
    if consulta == Loop:
        achado = True
        break
    else:
        achado = False 
        
print('o nome',consulta,'foi achado')
'''
'''
convidados = ["Ana", "Bruno", "Caio", "Beatriz", "Daniel"]
busca = input("Digite o nome para buscar: ").capitalize()

# Criamos uma variável para marcar se achamos ou não
achou = False

# O 'for' vai visitar cada nome da lista, um por um
for nome in convidados:
    if nome == busca:
        achou = True
        break  # Se achou, não precisa continuar olhando os outros

# Depois que o loop terminar, verificamos o nosso "vigia"
if achou:
    print(f"Sucesso! {busca} está na lista.")
else:
    print(f"Ops! {busca} não foi encontrado.")'''
    
    
'''    
soma = int()
for Loop in range(1,51):
    soma = soma + Loop
print (soma)   
'''

'''
Lista = [1,2,3,4,5]
print(max(Lista))
print(min(Lista)) 
'''

print('calculo de fatorial de um número')
numero = int(input('digite o número '))
fatorial = int(1)
for Loop in range (numero, 0 , -1):
    fatorial = fatorial*numero
    numero = numero -1 
print(fatorial)

