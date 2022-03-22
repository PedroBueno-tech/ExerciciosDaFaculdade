agua = float(input("Digite o valor da sua conta de Água: "))
luz = float(input("Digite o valor da sua conta de Luz: "))
internet = float(input("Digite o valor da sua conta de Internet: "))

sal = float(input("Digite o valor do seu salário: "))

total = agua+luz+internet

print(f"Água: {agua} \nLuz: {luz} \nInternet: {internet} \nTotal: {total}")

if(sal < total):
    print(f"O salário de R${sal} não é o suficiente para pagar a conta de R${total}")
else:
    print("O salário é suficiente para pagar todas as contas, após o pagamento sobrará: ", sal-total)