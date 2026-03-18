#definição de novas funções

#sem parâmetro
'''
def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()
'''


#com parâmetro
'''
def <nome>(<param_1>, <param_2>, ..., >param_n>):
    <instruções>
'''

'''
def media(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3)/3
    print(calculo)

media(1,2,3)   


nota1 = 8
nota2 = 7
nota3 = 6

media(nota1,nota2,nota3)
media(nota_1 = nota1,nota_2 = nota2,nota_3 = nota3)
'''


#com return
'''
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo
    
resultado = media (notas)
print(resultado)
'''



#retorno de função como tupla, e associação desses valores à variáveis.
'''
notas = [6.0, 7.0, 9.0, 5.0]

def boletim(lista):
    media = sum(lista) / len(lista)
    
    if media >=6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    
    return (media,situacao) 

resultado = boletim(notas)
print(resultado)

media, situacao = boletim(notas)

print(f'O estudante atingiu uma média de {media} e foi {situacao}.')
'''