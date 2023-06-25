#https://olimpiada.ic.unicamp.br/pratique/p1/2007/f1/perdida/

#Joãozinho adora quebra-cabeças, essa é sua brincadeira favorita. O grande problema, porém, é que às vezes o jogo vem com uma peça faltando. Isso irrita bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar uma peça de reposição ao fabricante do jogo. Sabendo que o quebra-cabeças tem N peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Joãozinho a saber qual peça ele tem de pedir.

num_pecas = int(input())
sequencia = input()

l_sequencia = []
for i in sequencia.split(): #sem o split a lista fica com espacos  ' '
  i = int(i)
  l_sequencia.append(i)

#l_sequencia.sort() ordem crescente

l_comparar = list(range(1, num_pecas+1)) #cria outra lista de 1 até o numero dado no input

print((sum(l_comparar)) - (sum(l_sequencia))) #ao somar todos os elementos de cada lista e subtrair pela outra, encontra a peça que falta