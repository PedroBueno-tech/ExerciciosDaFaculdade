print("Entrada: ")
print("Cordenadas de um ponto P (x, y)")
x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print(f"O ponto ({x}, {y}) pertence ao primeiro quadrante")

elif x < 0 and y > 0:
    print(f"O ponto ({x}, {y}) pertence ao segundo quadrante")

elif x < 0 and y < 0:
    print(f"O ponto ({x}, {y}) pertence ao terceiro quadrante")
    
else:
    print(f"O ponto ({x}, {y}) pertence ao quarto quadrante")