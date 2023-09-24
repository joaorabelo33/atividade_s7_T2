def main():
    numero_um  = input()
    numero_dois = input() 
    numero_tres = input()

    lista_exemplo = [numero_um,numero_dois,numero_tres]
    lista_tesste = sorted(lista_exemplo)

    print(lista_tesste[0])
    print(lista_tesste[1])
    print(lista_tesste[2])



if __name__ == '__main__':
    main()