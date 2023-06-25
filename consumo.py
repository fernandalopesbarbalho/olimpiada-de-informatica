#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

distancia = int(input())
combustivel = float(input())

print("%.3f" % (distancia / combustivel), "km/l")