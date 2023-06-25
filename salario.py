#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

funcionario = int(input())
horas = int(input())
valor_hora = float(input())

print("NUMBER =", funcionario)
print("SALARY = U$", "%.2f" % (horas * valor_hora))