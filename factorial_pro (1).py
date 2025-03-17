import argparse


def fact(n: int) -> int:
    """
    Esta función calcula el factorial de un número entero
    utilizando recursión
    :param n: Número entero para cálculo de factorial
    :return: factorial del número n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Entero para cálculo del factorial')
    parser.add_argument('n',
                        action='store',
                        type=str,
                        help='Entero para calcular el factorial; debe ser mayor o igual que cero')
    args = parser.parse_args()
    try:
        n = int(args.n)
        if n < 0:
            print("Argumento Inválido")
        else:
            print(f'El factorial de {n} es {fact(n)}')

    except:
        print("Argumento Inválido")
