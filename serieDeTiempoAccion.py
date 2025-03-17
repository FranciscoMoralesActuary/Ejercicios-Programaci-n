import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os


def leerDatos(nombreAccion: str) -> pd.DataFrame:
    ruta = '/home/jose/Documentos/bd/stocks/full_history'
    preciosAccion = pd.read_csv(os.path.join(ruta,
                                             f'{nombreAccion}.csv'))
    if len(preciosAccion) < 30:
        print("No hay suficientes datos")
        return pd.DataFrame()
    else:
        preciosAccion['date'] = pd.to_datetime(preciosAccion['date']).dt.date
        preciosAccion = preciosAccion.sort_values(by='date',
                                                  ascending=False)
        preciosAccion = preciosAccion.head(30)[['date', 'close']].set_index('date')
        return preciosAccion


def crearGrafico(nombreAccion: str):
    datos = leerDatos(nombreAccion)
    if len(datos) == 0:
        print("No se puede generar gráfico")
    else:
        plt.figure()
        datos.plot(color='purple', marker='o')
        plt.title(nombreAccion)
        plt.xticks(rotation=90)
        plt.savefig(f'graficos/{nombreAccion}.png')
        plt.close()
        print(f'Gráfico de la acción {nombreAccion} generado exitosamente')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Acción a graficar')
    parser.add_argument('accion',
                        action='store',
                        type=str,
                        help='Clave de cotización de la acción')
    args = parser.parse_args()
    crearGrafico(args.accion)
