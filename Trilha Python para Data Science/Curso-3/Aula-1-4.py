# %%

import numpy as np
import matplotlib.pyplot as plt

# O 'r' antes das aspas resolve o problema do caminho no Windows
dado = np.loadtxt(r'C:\Users\ESTAGI-02\Documents\Repos\Python\Curso-3\apples_ts.csv', delimiter=',', usecols=np.arange(1, 88, 1))

#aula 1-7
'''
print(dado.ndim)
print('\n\n')
print(dado.size)
print('\n\n')
print(dado.shape)
print('\n\n')
'''
dado_transposto = dado.T
#print(dado)
#print(dado_transposto)

datas = dado_transposto[:,0]
precos = dado_transposto[:,1:6]



#plt.plot(datas,precos[:,0])


Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]


#aula 2-4


Moscow.shape


Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

'''
plt.plot(np.arange(1,13,1), Moscow_ano1)

plt.plot(np.arange(1,13,1), Moscow_ano2)

plt.plot(np.arange(1,13,1), Moscow_ano3)

plt.plot(np.arange(1,13,1), Moscow_ano4)

plt.legend(['ano1','ano2','ano3','ano4'])
'''
'''
np.array_equal(Moscow_ano3, Moscow_ano4)

np.allclose(Moscow_ano3,Moscow_ano4, 0.01)
'''

#Aula 2-8
plt.plot(datas, Kaliningrad)

sum(np.isnan(Kaliningrad))



Kaliningrad[4] = (Kaliningrad[3]+Kaliningrad[5])/2 

#np.mean(Kaliningrad[3],Kaliningrad[5])


np.mean(Moscow)
np.mean(Kaliningrad)





# %%


