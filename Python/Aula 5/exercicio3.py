nomeProd = input("Digite o nome do produto: ")
valProd = float(input("Digite o valor do produto: "))

if(valProd < 10):
    valProd = valProd*1.70
elif(valProd >= 10 and valProd < 30):
    valProd = valProd*1.50
elif(valProd >= 30 and valProd < 50):
    valProd = valProd*1.40
else:
    valProd = valProd*1.30

print(f"Produto: {nomeProd}\nValor de venda: {valProd}")