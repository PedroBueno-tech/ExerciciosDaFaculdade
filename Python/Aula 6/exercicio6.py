
n1 = float(input("Digite a primeira nota parcial: "))
n2 = float(input("Digite a segunda nota parcial: "))
media = (n1 + n2) / 2


if(media >= 9 and media <= 10):
    conceito = "A"
elif(media >= 7.5 and media <= 8.9):
    conceito = "B"
elif(media >= 6 and media <=7.4 ):
    conceito = "C"
elif(media >= 4 and media <= 5.9):
    conceito = "D"
else:
    conceito = "E"


if(conceito == "A" or conceito == "B" or conceito == "C"):
    mensagem = "Aprovado"
else:
    mensagem = ("Reprovado")

print(f"Conceito: {conceito}\nMensagem: {mensagem}")



