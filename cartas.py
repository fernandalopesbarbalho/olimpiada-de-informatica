#https://olimpiada.ic.unicamp.br/pratique/ps/2014/f1/cartas/

#Recebe 5 números inteiros e verifica se estão em ordem crescente (imprimindo "C"), descrescente (imprimindo "D") ou fora de ordem (imprimindo "N").

cartas = input()

lista = [] #lista que mantem a ordem original
listaC = [] #lista que sera em ordem crescente
listaD = [] #lista que sera em ordem decrescente

for i in cartas.split(): #separa a str
  i = int(i) #transforma em int
  lista.append(i)
  listaC.append(i)
  listaD.append(i)

listaC.sort() #ordem crescente
listaD.sort(reverse=True) #ordem decrescente

if lista == listaC:
  print("C")

elif lista == listaD:
  print("D")

else:
  print("N") #sem ordem