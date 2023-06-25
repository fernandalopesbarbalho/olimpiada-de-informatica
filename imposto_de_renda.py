#Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$. Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo. 

#Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais. 

#Sendo que de 0.00 até 2000.00 é isento, de 2000.01 até 3000.00 a taxa é de 8%, de 3000.01 até 4500.00 a taxa é de 18% e acima de 4500.00 a taxa é de 28%. 

salario = float(input())

if salario >= 0 and salario <= 2000:
  print("Isento")

elif salario > 2000 and salario <= 3000:
  print("R$", "%.2f" % ((salario - 2000) * 0.08))

elif salario > 3000 and salario <= 4500:
  print("R$", "%.2f" % ((salario - 3000) * 0.18 + 80))

elif salario > 4500:
  print("R$", "%.2f" % ((salario - 4500) * 0.28 + 350))