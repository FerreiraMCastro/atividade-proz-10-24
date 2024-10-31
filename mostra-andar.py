#Imprimir todos os números exceto 13 (laço "for in range")
for i in range(1,21):
     if(i != 13):
      print(i)

#imprimir todos os números exceto o 13 em ordem descente
for i in range(20,1,-1):
    if(i != 13):
     print(i)
    
#Imprimir todos os números exceto o 13 (laço "while")
andar = 1
while(andar <= 20):
    if(andar != 13):
     print(andar)
    andar+=1 
