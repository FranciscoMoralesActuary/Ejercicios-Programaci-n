n = input("Ingresa un número: ")
try:
    n = int(n)
    if n >= 0:
        if (n == 0) or (n == 1):
            print(1)
        else:
            fact = 1
            i = n
            while i >= 2:
                fact *= i  # fact = fact * i
                i -= 1  # i = i - 1
            print(fact)

    else:
        print(f'El entero {n} no es válido')
except:
    print("Debes ingresar un número entero")
