#Este es un programa que lee una lista de numeros positivos y regresa el maximo numero que se puede formar

def leer_datos(a):
    numeros = []
    for i in range(a):
        numeros.append(int(input(f'Ingresa el numero {i}:')))
    return numeros

def ordenar (lista):
    numg = "".join(str(a) for a in lista)
    numeros1 = [int(a) for a in str(numg)]
    numeros1.sort(reverse=True)
    numeros1
    numfinal = "".join(str(a) for a in numeros1)
    return numfinal


if __name__ == '__main__':
    n = int(input("Ingresa la cantida de numeros que quieres ingresar a la lista: "))
    numeros=leer_datos(n)
    nf=ordenar(numeros)
    print(f'El numero mas grande es {nf}')
