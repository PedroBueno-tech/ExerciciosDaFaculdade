nome = input("Digite seu nome: ")
horas = int(input("Digite as horas [0-23]: "))

if horas >=5 and horas <= 12:
    print(f"Bom dia, {nome}")
elif horas >=13 and horas <= 18:
    print(f"Boa tarde, {nome}")
elif horas <=4 or horas >= 19:
    print(f"Boa noite, {nome}")
else:
    print("Horario inválido")