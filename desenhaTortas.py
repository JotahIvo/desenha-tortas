import turtle
import math

#Calcula o angulo exato entre o traço e o segmento principal
def achaAngulo(n):
    beta = (360 / n) / 2

    return 180 - 90 - beta


#Desenha o poligono principal de n segmentos
def desenhaPoligono(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


#Calcula o tamanho do traço que na angulação já calculada, chega ao centro do polígono
def calculaTraco(length, angulo):
    return (length / 2) / math.cos(math.radians(angulo))


#Faz o turtle voltar a origem
def voltarSegmento(t, traco):
    t.rt(180)
    t.fd(traco)


#Ajusta a angulação do turtle para ir para o poróximo traço
def ajustaAngulacao(t, angulo, length):
    t.lt(180 - angulo)
    t.fd(length)


#Desenha o primeiro traço
def primeiroTraco(t, angulo, traco, length):
    t.lt(angulo)
    t.fd(traco)

    voltarSegmento(t, traco)
    ajustaAngulacao(t, angulo, length)


#Ajusta o ângulo do traço e o desenha
def desenhaTracos(t, angulo, traco):
    t.lt(180 - (angulo * 2))
    t.lt(angulo)
    t.fd(traco)


#Função que faz todo o desenho
def desenhaTorta(t, n, length):
    desenhaPoligono(t, n, length)

    angulo = achaAngulo(n)
    traco = calculaTraco(length, angulo)

    #Desenhar o primeiro traço:
    primeiroTraco(t, angulo, traco, length)

    #Desenhar os demais traços
    for i in range(n - 1):
        desenhaTracos(t, angulo, traco)
        voltarSegmento(t, traco)
        ajustaAngulacao(t, angulo, length)


def main():
    bob = turtle.Turtle()

    n = 8
    length = 50

    desenhaTorta(bob, n, length)
  
    print(bob)
    turtle.mainloop()

if __name__ == '__main__':
    main()