#(Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido. Nenhum dígito é ímpar. Apenas um dígito é ímpar. Os dois dígitos são ímpares.)

def imp(numero):
    qtd_im= 0
    unidade = numero[0]
    dezena = numero[1]
    
    if (int(unidade)%2 !=0):
        qtd_im += 1
    if (int(dezena)%2!=0):
        qtd_im += 1
    return qtd_im

def quantidade_imp (numero):   
    if (imp(numero)==0):
        resposta = 'Nenhum dígito é ímpar.'
    if (imp(numero)==1):
        resposta ='Apenas um dígito é ímpar.'
    if (imp(numero)==2):
        resposta = 'Os dois dígitos são ímpares.'
    return resposta

numero= input()
if(len(numero) == 2):
    print(quantidade_imp(numero))
elif(True):
    print(0)