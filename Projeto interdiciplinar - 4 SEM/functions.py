def transform(base):
    if base != 16:
        number = input()
        stringSize = len(number) -1
        y = len(number) -1
        x = 0
        acummulator = 0
        while x <= stringSize:
            print(number[x])
            
        
            acummulator += int(number[x]) * (base**y)
            y -= 1
            x += 1
        print(acummulator)
    else:
        number = input()

        acummulator = 0
        stringSize = len(number) -1
        x = 0
        transformed = []
        inDecimal = [10,11,12,13,14,15]
        inHexa = ["A", "B", "C", "D", "E", "F"]


        while x <= stringSize:
            
            if ((number[x].upper() == "A") or (number[x].upper()  == "B") or (number[x].upper()  == "C") or (number[x].upper()  == "D") or (number[x].upper()  == "E") or (number[x].upper()  == "F")):
                j = 0
                while j < 6:
                    if(number[x].upper() == inHexa[j]):
                        transformed.append(inDecimal[j])
                    j+=1
            else:
                transformed.append(number[x])
            x+=1
        x = 0
        y = len(number) -1
        while x <= stringSize:
            acummulator += int(transformed[x]) * (16**y)
            y -= 1
            x += 1
        print(acummulator)