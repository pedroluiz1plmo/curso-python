'''
    utilização de LAMBDA
'''

#declaracao 1

nota = float(input('digite a nota do estudante: '))
def qualitativo(x): #criacao da funcao lambda
    return x + 0.5

qualitativo(nota)



#declaracao 2

nota = float(input('digite a nota do estudante: '))

qualitativo = lambda x: x+0.5

qualitativo(nota)


#aplicação

N1 = float(input('digite a nota do estudante: '))
N2 = float(input('digite a nota do estudante: '))
N3 = float(input('digite a nota do estudante: '))


media_ponderavel = lambda x, y, z: (x * 3 + y*2+ z*5)/10
media_estudante = media_ponderavel(N1,N2,N3)


print(f'O estudante atingiu a média de {media_estudante}')


#mapeando valores
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)
notas_atualizadas = list(notas_atualizadas)
print(notas_atualizadas)
