altura = float(input("Digite sua altura: "))
sexo = input("Digite o sexo m/f: ")

if sexo.upper() == "M":

    pesoIdeal = (72.7*altura)-58
    print(f"Peso ideal é igual a: {pesoIdeal:.2f}")
elif sexo.upper() == "F":
    pesoIdeal = (62.1*altura)-44.7
    print(f"Peso ideal é igual a: {pesoIdeal:.2f}")