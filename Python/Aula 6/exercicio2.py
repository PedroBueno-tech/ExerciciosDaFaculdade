segundos = int(input("Digite a quantiade de segundos: "))
horas = 0
minutos = 0

horas = (segundos//60)//60

segundos = segundos%3600

minutos = (segundos//60)

segundos = (segundos%60)

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")