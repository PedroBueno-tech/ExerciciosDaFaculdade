h = float(input("Digite a altura da pirâmide: "))
baseMenor = float(input("Digite o valor da base menor: "))
baseMaior = float(input("Digite o valor da base maior: "))

volume = h/3*(baseMaior**2 + baseMenor**2 + (baseMaior**2 * baseMenor**2)**0.5)

print("O volume do tronco da pirâmide é igual a: ", volume)