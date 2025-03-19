# Programa desarrollado por Jeison Garcia Arreaga

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Args:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento (por defecto es 10%).

    Returns:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def mostrar_resultado(monto, porcentaje_descuento):
    """Muestra el resultado del cálculo de descuento."""
    descuento = calcular_descuento(monto, porcentaje_descuento)
    monto_final = monto - descuento
    print(f'Monto original: ${monto:.2f}')
    print(f'Descuento aplicado ({porcentaje_descuento}%): ${descuento:.2f}')
    print(f'Monto final a pagar: ${monto_final:.2f}')
    print('-' * 40)


def main():
    print("Sistema de Cálculo de Descuentos - Jeison Garcia Arreaga\n")

    # Primera compra con descuento predeterminado
    monto_1 = 1200
    mostrar_resultado(monto_1, 10)

    # Segunda compra con un descuento personalizado
    monto_2 = 2000
    porcentaje_descuento_2 = 15
    mostrar_resultado(monto_2, porcentaje_descuento_2)


if __name__ == "__main__":
    main()
