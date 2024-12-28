import numpy as np
# Exemplo de uso do numpy para calcular a média artimetica 
dados = [1, 2, 3, 4, 5]
media = np.mean(dados)
print(f"A média é: {media}")




pesos= [1,2,3,4]

valores =  [12,3,4,45]


somatorio =  [valores[i]*pesos[i] for i in range(0,len(pesos))]
somaharmonica = sum(somatorio)/sum(pesos)

print(f"A média harmoica é : {somaharmonica}")




