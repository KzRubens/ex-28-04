salarioatual = float(input("Digite o salário do colaborador: R$"))

if salarioatual <= 280:
  reajuste = salarioatual * 0.20
  porc = ("20%")

elif salarioatual >= 280 and salarioatual <= 700:
  reajuste = salarioatual * 0.15
  porc = ("15%")

elif salarioatual >= 700 and salarioatual <= 1500:
  reajuste = salarioatual * 0.10
  porc = ("10%")

elif salarioatual >= 1500:
  reajuste = salarioatual * 0.05
  porc = ("5%")

  novo_salario = salarioatual - reajuste

print(f"O salario inicial: R${salarioatual}")
print(f"Foi aplicado o valor de {porc} em cima seu salário.")
print(f"Foi aumentado o valor de R${reajuste} no seu salário.")
print(f"Salário atual: R${novo_salario}.")