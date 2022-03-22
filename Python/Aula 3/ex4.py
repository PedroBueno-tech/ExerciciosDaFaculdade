valorPrestacao = float(input("Digite o valor da prestação: "))

multa =  float(input("Digite o valor da porcentagem da multa: "))

qtdeDias = float(input("Digite o valor de dias atrasados: "))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print("O valor atual da prestação está em: ", prestacao)
