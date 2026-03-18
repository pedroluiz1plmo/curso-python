#RAISE
# 
# raise ValueError("A lista de notas deve possuir dez elementos")

'''
Função para calcular a média de notas passadas por uma lista

lista: list, default[0]
    Lista com as notas para calcular a média
    return calculo: float
    Média calculada
''' 

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas")
    return calculo


notas = [6, 7, 8, 8]
#notas_erro = [5,6,6,7,8]
resultado = media(notas)

print(resultado)

#resulta_erro = media(notas_erro)
#print(resulta_erro)


try:
    notas = [6, 7, 8, 9]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceito valores numéricos")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print('A consulta foi encerrada')