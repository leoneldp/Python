# -*- coding: utf-8 -*-
import unittest

class MenorPago(Exception):
    def __init__(self, msj):
        self.msj = msj


class Ticket(object):
    """Clase para generar y operar sobre el ticket"""

    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, codigo, nombre, precio):
        """Genera una instancia de la clase producto con los parámetros del mismo.
        Agrega el producto con el formato adecuado a la matriz lista_productos.
        Devuelve el producto formateado como lista"""

        item_a_agregar = Producto(codigo, nombre, precio)
        self.lista_productos.append([item_a_agregar.codigo, item_a_agregar.nombre, item_a_agregar.precio])
        cantidad_items = len(self.lista_productos)
        return self.lista_productos[cantidad_items-1]

    def calcular_subtotal(self):
        """Suma los ítems agregados al ticket hasta el momento y devuelve el subtotal"""

        self.subtotal = 0
        for i in range(len(self.lista_productos)):
            self.subtotal += self.lista_productos[i][2]
        return self.subtotal

    def finalizar_compra(self, descuento):
        """Genera el ticket con los items en formato para imprimirse.
        Calcula el subtotal y el monto a descontar según el parámetro.
        Calcula el total e imprime el ticket en pantalla.
        Devuelve el ticket impreso para verificar en el test"""

        self.ticketImpreso=[]
        for i in range(len(self.lista_productos)):
            self.ticketImpreso.append(str(self.lista_productos[i][0]).ljust(6) + self.lista_productos[i][1].ljust(20,".") + "$ " + str("{0:.2f}".format(self.lista_productos[i][2])).rjust(6))
        self.subtotal_compra = self.calcular_subtotal()
        self.descuento_compra = self.calcular_descuento(descuento, self.subtotal_compra)
        self.total_descontado = self.subtotal_compra - self.descuento_compra

        self.ticketImpreso.append(("SUBTOTAL:" + ("$ " + str("{0:.2f}".format(self.subtotal_compra))).rjust(25, ".")))
        self.ticketImpreso.append(f"DESCUENTO {int(descuento*100)}%:" + ("$ " + (str("{0:.2f}".format(self.descuento_compra))).rjust(6)).rjust(20, "."))
        self.ticketImpreso.append(("TOTAL:" + ("$ " + str("{0:.2f}".format(self.total_descontado))).rjust(28, ".")))
        

        return self.ticketImpreso

    def calcular_descuento(self, descuento, precio):
        """Calcula el valor a descontar según el porcentaje (en decimal) aplicado como descuento"""

        self.descuento = precio*descuento
        return self.descuento

    def pagar_compra(self, paga_con):
        """Se asegura que el monto con el que paga el cliente no sea menor a lo que debe pagar.
        En caso que así lo fuera lanza la excepción MenorPago.
        Calcula el vuelto e imprime en pantalla paga_con y vuelto"""

        if paga_con < self.total_descontado:
            raise MenorPago("El pago es menor al total")
        self.vuelto = (paga_con - self.total_descontado)
        print("\nPaga con: "+ ("$ {0:.2f}".format(paga_con)).rjust(10))
        print("Cambio: " + ("$ {0:.2f}".format(self.vuelto)).rjust(12))
        return self.vuelto


class Producto(object):
    """Clase para generar cada Producto a ingresar al ticket
    Comprueba que codigo sea un entero,
    nombre sea un string y precio un entero o float.
    En caso contrario, lanza la excepción ValueError para cada caso"""

    def __init__(self, codigo, nombre, precio):
        if type(codigo) == int:
            self.codigo = codigo
        else:
            raise ValueError("El código debe ser un Entero")
        if type(nombre) == str:
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una Cadena")
        if type(precio) == float or type(precio) == int:
            self.precio = precio
        else:
            raise ValueError("El precio debe ser una Entero o Decimal")


class CajaAlmacenTestCase(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket()   # crea el nuevo ticket

    def test_agregar_producto(self):
        result = self.ticket.agregar_producto(301, "Mayonesa", 50.14)
        self.assertEqual([301, "Mayonesa", 50.14], result)

    def test_agregar_producto_exceptions(self):
        with self.assertRaises(ValueError):
            self.ticket.agregar_producto("trescientosUno", "Mayonesa", 50.14)
        with self.assertRaises(ValueError):
            self.ticket.agregar_producto(301, True, 50.14)
        with self.assertRaises(ValueError):
            self.ticket.agregar_producto(301, "Mayonesa", "Cincuenta")
       
    def test_calcular_subtotal(self):
        self.ticket.agregar_producto(301, "Mayonesa", 50.14)
        self.ticket.agregar_producto(302, "Aceite", 120.00)
        result = self.ticket.calcular_subtotal()
        self.assertEqual(170.14, result)


class FinalizarCompraTestCase(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket()   # crea el nuevo ticket
        self.ticket.agregar_producto(301, "Mayonesa", 50.14)
        self.ticket.agregar_producto(302, "Aceite", 120.00)
        self.ticket.agregar_producto(303, "Yogurt", 98.35)
        self.ticket.agregar_producto(304, "Café", 340.70)
        self.ticket.agregar_producto(305, "Hamburguesas", 276.35)

    def test_finalizar_compra(self):
        result = self.ticket.finalizar_compra(0.1)
        self.assertEqual([
            "301   Mayonesa............$  50.14",
            "302   Aceite..............$ 120.00", 
            "303   Yogurt..............$  98.35",
            "304   Café................$ 340.70",
            "305   Hamburguesas........$ 276.35",
            "SUBTOTAL:.................$ 885.54",
            "DESCUENTO 10%:............$  88.55",
            "TOTAL:....................$ 796.99"
        ], result)

        print("\nCÓD.  PRODUCTO              PRECIO") # comienza impresión del ticket para referencia visual
        for t in range(len(self.ticket.ticketImpreso)):
            print(self.ticket.ticketImpreso[t])

        vuelto_pago = self.ticket.pagar_compra(800.0)
        self.assertEqual("3.01", "{0:.2f}".format(vuelto_pago))

    def test_pagar_compra_exceptions(self):
        self.ticket.finalizar_compra(0.1)
        with self.assertRaises(MenorPago):
            self.ticket.pagar_compra(700.0)


if __name__ == '__main__':
    unittest.main()

