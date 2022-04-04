print("Digite a idade: ")
idade = int(input())

if(idade <= 16):
    print("Não-eleitor")
elif(idade >= 18 and idade < 65):
    print("Eleitor obrigatório")
else:
    print("Eleitor Facultativo")