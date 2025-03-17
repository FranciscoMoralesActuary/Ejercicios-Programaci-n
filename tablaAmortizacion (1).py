import argparse
import numpy as np
from numpy_financial import pmt
import pandas as pd


def convertirMonto(monto: str) -> float:
    """
    Convierte el monto del préstamo a flotante
    :param monto: monto del crédito
    :return: monto en formato flotante
    """
    try:
        monto = float(monto)
        return monto
    except Exception as e:
        print(e)
        return None


def convertirTasa(tasa: str) -> float:
    """
    Convierte tasa de interés
    :param tasa: tasa en formato XX.XX%
    :return: tasa de interés como número real
    """
    if (tasa[-1] == '%') and ('.' in tasa):
        tasa = float(tasa[:-1]) / 100
        return tasa
    else:
        return None


def convertirPlazo(plazo: str) -> int:
    """
    Convierte el plazo a entero
    :param plazo: plazo en semanas
    :return: plazo en formato entero
    """
    try:
        plazo = int(plazo)
        return plazo
    except Exception as e:
        print(e)
        return None


def calcularTabla(monto: float, plazo: int, tasa: float) -> pd.DataFrame:
    """
    Calcula la tabla de amortización del crédito solicitado
    :param monto: monto del crédito
    :param plazo: plazo en semanas
    :param tasa: tasa de interés anual
    :return: DataFrame con cada iteración de la tabla de amortización.
    """
    # Iteración inicial
    pago = -np.round(pmt(tasa / 52, plazo, monto), 2)
    saldoInicial = monto
    interes = saldoInicial * tasa / 52
    capital = pago - interes
    iva = interes * 0.16
    pagoConIva = capital + interes + iva
    saldoFinal = saldoInicial - capital
    iteracion = tuple(map(lambda x: np.round(x, 2),
                          (saldoInicial,
                           pago,
                           capital,
                           interes,
                           iva,
                           pagoConIva,
                           saldoFinal)))
    listaIteraciones = [iteracion]
    # Iteraciones posteriores
    for _ in range(plazo - 1):
        saldoInicial = saldoFinal
        interes = saldoInicial * tasa / 52
        capital = pago - interes
        iva = interes * 0.16
        pagoConIva = capital + interes + iva
        saldoFinal = saldoInicial - capital
        iteracion = tuple(map(lambda x: np.round(x, 2),
                              (saldoInicial,
                               pago,
                               capital,
                               interes,
                               iva,
                               pagoConIva,
                               saldoFinal)))
        listaIteraciones.append(iteracion)
    tablaAmortizacion = pd.DataFrame(listaIteraciones,
                                     columns=['Saldo Inicial',
                                              'Pago',
                                              'Capital',
                                              'Interés',
                                              'IVA',
                                              'Pago +Iva',
                                              'Saldo Final'])
    tablaAmortizacion.insert(0, 'i', tablaAmortizacion.index + 1)
    return tablaAmortizacion


def exportarExcel(tablaAmortizacion: pd.DataFrame):
    """
    Exporta tabla de amortización a Excel
    :param tablaAmortizacion: DataFrame con las iteraciones
    :return: None
    """
    with pd.ExcelWriter('amort.xlsx') as xl:
        tablaAmortizacion.to_excel(xl,
                                   index=False,
                                   sheet_name='Tabla de Amortización')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parámetros de Tabla de Amortización')
    parser.add_argument('monto',
                        action='store',
                        type=str,
                        help='Monto del préstamo')
    parser.add_argument('tasa',
                        action='store',
                        type=str,
                        help='Tasa de interés anual en formato XX.XX%')
    parser.add_argument('plazo',
                        action='store',
                        type=str,
                        help='Plazo en semanas')
    args = parser.parse_args()

    monto, tasa, plazo = convertirMonto(args.monto), \
                         convertirTasa(args.tasa), \
                         convertirPlazo(args.plazo)

    exportarExcel(calcularTabla(monto, plazo, tasa))
