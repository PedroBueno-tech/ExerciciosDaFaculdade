n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

opcao = input("Digite a operação matemática desejada (+, -, *, /): ")

if opcao == "+":
    n1 = n1 + n2
elif opcao == "-":
    n1 = n1 - n2
elif opcao == "*":
    n1 = n1 * n2
elif opcao == "/":
    n1 = n1 / n2
else:
    print("Opção inválida")

print(f"A operação de {opcao} deu o resultado de: {n1}")