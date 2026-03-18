import matplotlib
import matplotlib.pyplot as plt
from random import choice as ch


estudantes = ["João","Maria","José"]
notas = [8.5,9,6.5]

plt.bar(x = estudantes, height= notas)



estudante = ch(estudantes)
print(estudante)