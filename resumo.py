def mostrar_numero():
    numero_valido = False
    print("escreva um numero menor ou igual a 100")
    
    while(numero_valido == False):
        try:
            num = int(input())
            if(num > 100):
                print("O numero precisa ser menor ou igual a 100")
            else:
                print("Boa! voce escolheu um numero: " +str(num))
                numero_valido = True
        except:
            print("O valor inserido deve ser um número inteiro")
    


mostrar_numero()

