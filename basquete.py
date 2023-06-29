#https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/basquete/

#Programa que recebe uma distância e imprime '1' se a distância for menor ou igual a 800, '2' se for entre 801 e 1400, ou '3' se for entre 1401 e 2000.

d = int(input())

if (d <= 800):
  print(1)

elif (800 < d and d <= 1400):
  print(2)

elif (1400 < d and d <= 2000):
  print(3)