#definir a função
def achar_elemento(elem,arr):
   achou = False
   cumprimento = len(arr)
   
   for i in range(cumprimento):
     if (arr[i] == elem):
         achou = True
         
   if(achou == True):
      print("Achei o nome: " + elem)
   else:
      print("Não achei o nome: " + elem)   
      
      
nomes = ["Maria", "cassio","felipe","juliana","jane"]
achar_elemento("Maria",nomes)
    
    
