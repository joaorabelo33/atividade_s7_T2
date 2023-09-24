def  numeros(numero):
    numeros_pares = 0
    unidade= numero[0]
    dezena = numero[1]
    centena= numero[2]

    if(int(unidade)%2==0): 
        numeros_pares+=1
    if(int(dezena)%2==0): 
        numeros_pares+=1
    if(int(centena)%2==0): 
        numeros_pares+=1   
        
    return numeros_pares


numero_inteiro = input()
    
if(len(numero_inteiro) == 3):
        print(numeros(numero_inteiro))
elif(True):
        print(0)




