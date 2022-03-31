import functions

isRunning = True

while isRunning:
    print("Escolha uma das opções abaixo")

    print("1 - Binario para decimal\n2 - Octal para decimal\n3 - Hexadecimal para decimal\n0 - sair ")
    choice = input()

    if(choice == "1"):
        print("Voce escolheu a opcao binario para decimal\n\nDigite o numero em binario")
        functions.transform(2)
    elif(choice == "2"):
        print("Voce escolheu a opcao octal para decimal\n\nDigite o numero em octal")
        functions.transform(8)
    elif(choice == "3"):
        print("Voce escolheu a opcao hexadecimal para decimal\n\nDigite o numero em hexadecimal")
        functions.transform(16)
    elif(choice == "0"):
        isRunning = False

        print("Obrigado pela escolha tenha um otimo dia")
    else:
        print("Opcao invalida, escolha uma opcao validas\n\n")
    

