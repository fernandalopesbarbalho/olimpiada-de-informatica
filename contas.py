#https://olimpiada.ic.unicamp.br/resultados/fase1/programacao/cadernos/

#Programa que recebe um número inteiro referente ao saldo disponivel de uma pessoa e também o valor de três contas a pagar, imprimindo o maior número de contas que é possível realizar o pagamento.

dinheiro = int(input())

acougue = int(input())
farmacia = int(input())
padaria = int(input())

if dinheiro >= acougue + farmacia + padaria:
    print(3)

elif dinheiro >= acougue + farmacia or dinheiro >= acougue + padaria or dinheiro >= farmacia + padaria:
    print(2)

elif dinheiro >= acougue or dinheiro >= farmacia or dinheiro >= padaria:
    print(1)

else:
    print(0)