# -*- coding: utf-8 -*-
import unittest

class Ticket(object):
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, codigo, nombre, precio):
        item_a_agregar = Producto(codigo, nombre, precio)
        self.lista_productos.append([item_a_agregar.codigo, item_a_agregar.nombre, item_a_agregar.precio])
        return self.mostrar_ultimo()
    
    def mostrar_ultimo(self):
        cantidad_items = len(self.lista_productos)
        return self.lista_productos[cantidad_items-1]
    
    def calcular_subtotal(self):
        self.subtotal = 0
        for i in range(len(self.lista_productos)):
            self.subtotal += self.lista_productos[i][2]
        return self.subtotal

    def calcular_descuento(self, descuento):
        self.descuento = self.subtotal_compra*descuento
        return self.descuento

    def finalizar_compra(self, descuento):
        self.ticketImpreso=[]
        for i in range(len(self.lista_productos)):
            self.ticketImpreso.append(str(self.lista_productos[i][0]).ljust(6) + self.lista_productos[i][1].ljust(20,".") + "$ " + str("{0:.2f}".format(self.lista_productos[i][2])).rjust(6))
        self.subtotal_compra = self.calcular_subtotal()
        self.descuento_compra = self.calcular_descuento(descuento)
        self.total_descontado = self.subtotal_compra - self.descuento_compra

        self.ticketImpreso.append(("SUBTOTAL:" + ("$ " + str("{0:.2f}".format(self.subtotal_compra))).rjust(25, ".")))
        self.ticketImpreso.append(f"DESCUENTO {int(descuento*100)}%:" + ("$ " + (str("{0:.2f}".format(self.descuento_compra))).rjust(6)).rjust(20, "."))
        self.ticketImpreso.append(("TOTAL:" + ("$ " + str("{0:.2f}".format(self.total_descontado))).rjust(28, ".")))

        print("\n")
        for t in range(len(self.ticketImpreso)):
            print(self.ticketImpreso[t])

        return self.ticketImpreso


class Producto(object):
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

    def test_finalizar_compra(self):
        self.ticket.agregar_producto(301, "Mayonesa", 50.14)
        self.ticket.agregar_producto(302, "Aceite", 120.00)
        self.ticket.agregar_producto(303, "Yogur", 98.35)
        self.ticket.agregar_producto(304, "Café", 340.70)
        self.ticket.agregar_producto(305, "Hamburguesas", 276.35)
        result = self.ticket.finalizar_compra(0.1)
        self.assertEqual([
            "301   Mayonesa............$  50.14",
            "302   Aceite..............$ 120.00", 
            "303   Yogur...............$  98.35",
            "304   Café................$ 340.70",
            "305   Hamburguesas........$ 276.35",
            "SUBTOTAL:.................$ 885.54",
            "DESCUENTO 10%:............$  88.55",
            "TOTAL:....................$ 796.99"

        ], result)


if __name__ == '__main__':
    unittest.main()


