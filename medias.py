import numpy as np
# Exemplo de uso do numpy para calcular a média artimetica 
dados = [1, 2, 3, 4, 5]
media = np.mean(dados)
print(f"A média é: {media}")


# usando  python puro
print(f'media artimetica simples: {(sum(dados)/len(dados))}')



#media artimetica ponderada
#consiste soma das multiplicacoes dos valores pelos respectivos pesos e dividir pela soma dos pesos
pesos= [1,2,3,4]
valores =  [12,3,4,45]

somatorio = [valores[i]*pesos[i] for i in range(0,len(pesos))]
mediaPonderada = sum(somatorio)/sum(pesos)

print(f"A média artimetica ponderada é : {mediaPonderada}")



#media harmonica ela e obtida atraves  da divicao do numero total de  elementos pela soma dos inversos dos elementos

x = [1,2,3,4,5]


media_harmonica = len(x)/sum([1/i for i in x])

print(f"A média harmonica é: {media_harmonica}")



#media harmonica ponderada 
#consiste em dividir o numero total de elementos pela soma dos inversos dos elementos multiplicados pelos respectivos pesos

gastos = [120, 100]
preco = [30, 50]

# Calculando a soma dos pesos divididos pelos valores
pesos_divididos_valores = [preco[i] / gastos[i] for i in range(len(gastos))]
media_harmonica_ponderada = sum(preco) / sum(pesos_divididos_valores)

print(f"A média harmônica ponderada é: {media_harmonica_ponderada:.2f}")






