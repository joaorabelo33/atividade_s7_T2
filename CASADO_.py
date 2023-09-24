nome = input()
civil= int(input())
nome=nome.strip()

if civil == 1:
    casal = input()
    casal= casal.strip()
    letras = len(nome)+ len(casal)
    print(letras)

elif civil == 2 :
    solteiro=len(nome)
    print(solteiro)
