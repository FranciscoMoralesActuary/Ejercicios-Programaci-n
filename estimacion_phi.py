import argparse
from math import sqrt


def nFibonacci(n: int) -> int:
    """
    Devuelve en n-ésimo número de Fibonacci
    :param n: Posición del número de Fibonacci a devolver
    :return: n-ésimo número de Fibonacci
    """

    if (n == 1) or (n == 2):
        return 1
    elif n < 1:
        return -1
    elif n > 2:
        return nFibonacci(n - 2) + nFibonacci(n - 1)


def estimarPhi(precision: float) -> tuple:
    """
    Estima el valor de la proporción áurea con cierto grado de precisión
    :param precision: valor flotante de precisión requerido
    :return: número de números de Fibonacci requeridos para la estimación
    y el valor de phi estimado.
    """
    phi = (1 + sqrt(5)) / 2
    phi0 = 0

    i = 2
    while abs(phi - phi0) > precision:
        phi0 = nFibonacci(i) / nFibonacci(i - 1)
        i += 1
    return i - 1, phi0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Valor de precisión')
    parser.add_argument('precision',
                        action='store',
                        type=str,
                        help='ingresar un valor decimal de precisión')
    args = parser.parse_args()
    try:
        n, phi = estimarPhi(float(args.precision))
        print("El valor estimado de phi es %f al usar %d números de Fibonacci" % (phi, n))
    except Exception as e:
        print(e)
        print("Nivel de precisión inválido")
