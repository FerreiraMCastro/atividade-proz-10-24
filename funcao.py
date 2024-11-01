def calculaDoisNumeros(num1, num2, sinal):
    soma = 1
    subtracao =2
    multiplicacao = 3
    divisao = 4
    
    if sinal == soma:
        return num1 + num2
    elif sinal == subtracao:
        return num1 - num2
    elif sinal == multiplicacao:
        return num1 * num2
    elif sinal == divisao:
        return num1 / num2
    else:
        return 0

meucalculo = calculaDoisNumeros(20, 10, 5) 
print(meucalculo) 

#def usuarioEscolhecalcular(num1, num2,operacao):
#   soma = 1
#   subtracao =2
#   multiprlicacao =3
#   divisao =4
#    sair = 0
    
#    if operacao == soma:
#        input("escolha dois numeros ")
#        soma = num1 + num2
#        return soma
#   elif operacao == subtracao:
#        input
       
    
       
    
    