print("Digite o horário do turno: \n D - Diurno \n N - noturno")
turno = input()

print("Digite o número de horas trabalhadas: ")
horas = float(input())

if (turno == "N" or turno == "n"):
    print("O valor total do salário devido as horas trabalhadas é igual a: ", horas*45.00)
else: 
    print("O valor total do salário devido as horas trabalhadas é igual a: ", horas*37.50)