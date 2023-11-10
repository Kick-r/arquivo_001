#Importações do código
import math
from random import uniform as unf

#Função de ativação
def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig

# Sorteia números de pesos
def random_pesos(pesos):
    for x in range(0, 4):
        for y in range(0, 2):
            pesos[x][y] = unf(-1, 1)

    return pesos

#Sorteia números de Bias
def random_bias(bias):
    for x in range(0, 5):
        bias[x] = unf(-10, 10)

    return bias

#função de erro
def loss_function(x, y):
    loss = x - y
    if loss < 0.0:
        loss = loss * -1

    return loss

#Define neuronios
entrada = [10, 10]
camada_oculta_1 = [0, 0]
camada_oculta_2 = [0, 0]
camada_de_saida = 0

#Define pesos e bias
pesos = [[0, 0], [0, 0], [0, 0], [0, 0]]
bias = [0, 0, 0, 0, 0]

#Define retorno esperado
resultado_esperado = 0.500

print('start: ')

#Loop que termina quando acha números de bias e pesos que retorna aproximadamente uo igual ao resultado esperado
while True:
    bias = random_bias(bias)
    pesos = random_pesos(pesos)

    camada_oculta_1[0] = sigmoid((entrada[0] * pesos[0][0]) + bias[0])
    camada_oculta_1[1] = sigmoid((entrada[1] * pesos[0][1]) + bias[1])

    camada_oculta_2[0] = sigmoid(((camada_oculta_1[0] * pesos[1][0]) + (camada_oculta_1[1] * pesos[1][1])) + bias[2])
    camada_oculta_2[1] = sigmoid(((camada_oculta_1[0] * pesos[2][0]) + (camada_oculta_1[1] * pesos[2][1])) + bias[3])

    camada_de_saida = sigmoid(((camada_oculta_2[0] * pesos[3][0]) + (camada_oculta_2[1] * pesos[3][1])) + bias[4])

    loss = loss_function(resultado_esperado, camada_de_saida)

    if loss < 0.0001:
        print('Entrada: ', entrada)
        print('Saída', camada_de_saida)
        break