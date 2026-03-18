#notas do estudante

notas = {'1º Trimestre': 8.5, '2º Trimestre': 9.5, '3º Trimestre': 7}

# Calculando a soma
soma = 0


for nota in notas.values():
    soma += nota

somatorio = sum(notas.values())
print(somatorio)


#usando a função embutida len()
qtd_notas = len(notas)


#calculando a média
media = somatorio / qtd_notas
media = round(media,1) #vai pegar só uma das casas decimais da média
print(media)