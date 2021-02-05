# -*- coding: utf-8 -*-
import unittest

class ProductoInexistente(Exception):
    """Excepción para cuando se ingresa un código de producto inexistente"""
    def __init__(self, msj):
        self.msj = msj


class MenorPago(Exception):
    """Excepción para cuando se paga con menor dinero que el valor del ticket"""
    def __init__(self, msj):
        self.msj = msj


class CajaRegistradora(object):
    """Clase para generar y operar sobre el ticket"""

    def __init__(self, lista_de_precios):
        self.lista_de_precios = lista_de_precios
        self.una_compra = Compra()

    def agregar_producto(self, codigo, descuento):
        """Busca con el código el precio y nombre del Producto
        Llama al método de la Compra para agregar el Producto
        En caso de haber descuento, reemplaza el precio del Producto por el descontado."""

        if descuento == 0:
            item_a_agregar = self.lista_de_precios.obtener_precio(codigo)
        else:
            item_a_agregar = self.lista_de_precios.obtener_precio(codigo)
            item_a_agregar[2] = self.lista_de_precios.obtener_precio_descontado(codigo, descuento)

        self.una_compra.agregar_producto(item_a_agregar)
        return item_a_agregar

    def calcular_subtotal(self):
        """Suma los ítems agregados al ticket hasta el momento y devuelve el subtotal"""

        self.subtotal = 0.0
        for i in range(len(self.una_compra.ticket)):
            self.subtotal += self.una_compra.ticket[i][2]
        return round(self.subtotal, 2)

    def calcular_total(self):
        return self.calcular_subtotal()
        
    def finalizar_compra(self):
        """Genera el ticket con los items en formato para imprimirse.
        Calcula el total e imprime el ticket en pantalla.
        Devuelve el ticket impreso para verificar en el test"""

        self.ticketImpreso=[]
        for i in range(len(self.una_compra.ticket)):
            self.ticketImpreso.append(str(self.una_compra.ticket[i][0]).ljust(6) + self.una_compra.ticket[i][1].ljust(20,".") + "$ " + str("{0:.2f}".format(self.una_compra.ticket[i][2])).rjust(6))
        self.total_compra = self.calcular_total()    
        self.ticketImpreso.append(("TOTAL:" + ("$ " + str("{0:.2f}".format(self.total_compra))).rjust(28, ".")))
        return self.ticketImpreso

    def pagar_compra(self, paga_con):
        """Se asegura que el monto con el que paga el cliente no sea menor a lo que debe pagar.
        En caso que así lo fuera lanza la excepción MenorPago.
        Calcula el vuelto e imprime en pantalla paga_con y vuelto"""

        if paga_con < self.total_compra:
            raise MenorPago("El pago es menor al total")
        self.vuelto = (paga_con - self.total_compra)
        print("\nPaga con: "+ ("$ {0:.2f}".format(paga_con)).rjust(10))
        print("Cambio: " + ("$ {0:.2f}".format(self.vuelto)).rjust(12))
        return self.vuelto


class Producto(object):
    """Clase para generar cada Producto a ingresar al ticket
    Comprueba que:
        -codigo sea un entero,
        -nombre sea un string
        -precio un entero o float.
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


class ListaDePrecios(object):
    """Clase que representa la lista de precios de la base de datos"""

    def __init__(self):
        self.lista_precios = []
    
    def incluir_en_lista(self, codigo, nombre, precio):
        """Genera una instancia de la clase producto con los parámetros del mismo.
        Agrega el producto con el formato adecuado a la matriz lista_precios.
        Devuelve la lista de precios"""

        item_a_agregar = Producto(codigo, nombre, precio)
        self.lista_precios.append([item_a_agregar.codigo, item_a_agregar.nombre, item_a_agregar.precio])
        return self.lista_precios

    def eliminar_de_lista(self):
        pass

    def obtener_precio(self, codigo):
        """Devuelve el precio y nombre de un producto a partir del código.
        Comprueba que el código sea un entero. 
        De lo contrario, levanta una excepción"""
        if type(codigo) == int:
            for i in range(len(self.lista_precios)):
                if self.lista_precios[i][0] == codigo:
                    return self.lista_precios[i]
            raise ProductoInexistente("El código del producto no corresponde a un producto de la Lista de Precios")
        else:
            raise ValueError("El código debe ser un Entero")


    def obtener_precio_descontado(self, codigo, descuento):
        """"Obtiene el precio descontado del producto a partir del código y el descuento
        Comprueba que el código sea un entero y que el descuento sea de 0.01 a 0.95
        De lo contrario, levanta las excepciones correspondientes"""

        if type(codigo) == int and type(descuento) == float and descuento >= 0.01 and descuento <= 0.95:
            self.precio_descontado = 0
            for i in range(len(self.lista_precios)):
                if self.lista_precios[i][0] == codigo:
                    self.precio_descontado = self.lista_precios[i][2]-self.lista_precios[i][2]*descuento
                    return self.precio_descontado
            print("noencontré")
        else:
            raise ValueError("El código debe ser un Entero y el descuento un Decimal de 0.01 a 0.95")


class Compra(object):
    """Clase que modela el ticket actual"""

    def __init__(self):
        self.ticket = []
    
    def agregar_producto(self, producto):
        """Agrega un producto al ticket actual"""
        
        self.ticket.append(producto)
        return self.ticket

    def eliminar_producto(self,codigo):
        pass





class CajaAlmacenTestCase(unittest.TestCase):
    def setUp(self):
        self.una_lista_de_precios = ListaDePrecios()
        self.una_lista_de_precios.incluir_en_lista(301, "Mayonesa", 50.14)
        self.una_lista_de_precios.incluir_en_lista(302, "Aceite", 120.00)
        self.una_lista_de_precios.incluir_en_lista(303, "Yogurt", 98.35)
        self.una_lista_de_precios.incluir_en_lista(304, "Café", 340.70)
        self.una_lista_de_precios.incluir_en_lista(305, "Hamburguesas", 276.35)
        self.una_lista_de_precios.incluir_en_lista(306, "Pan", 173.50)
        self.una_caja_registradora = CajaRegistradora(self.una_lista_de_precios)

    def test_agregar_producto(self):
        result = self.una_caja_registradora.agregar_producto(301, 0)
        self.assertEqual([301, "Mayonesa", 50.14], result)

    def test_agregar_producto_con_descuento(self):
        result = self.una_caja_registradora.agregar_producto(301, 0.1)
        self.assertEqual([301, "Mayonesa", 45.126], result)

    def test_agregar_producto_exceptions(self):
        with self.assertRaises(ValueError):
            self.una_caja_registradora.agregar_producto("trescientosUno", 0)
        with self.assertRaises(ValueError):
            self.una_caja_registradora.agregar_producto(True, 0)
        with self.assertRaises(ValueError):
            self.una_caja_registradora.agregar_producto(301, "0")
        with self.assertRaises(ProductoInexistente):
            self.una_caja_registradora.agregar_producto(310, 0)

    def test_calcular_subtotal(self):
        self.una_caja_registradora.agregar_producto(301, 0)
        self.una_caja_registradora.agregar_producto(302, 0)
        result = self.una_caja_registradora.calcular_subtotal()
        self.assertEqual(170.14, result)

    def test_calcular_subtotal_con_descuento(self):
        self.una_caja_registradora.agregar_producto(306, 0.2)
        self.una_caja_registradora.agregar_producto(304, 0.2)
        result = self.una_caja_registradora.calcular_subtotal()
        self.assertEqual(411.36, result)

    def test_calcular_total(self):
        self.una_caja_registradora.agregar_producto(303, 0)
        self.una_caja_registradora.agregar_producto(304, 0)
        result = self.una_caja_registradora.calcular_subtotal()
        self.assertEqual(439.05, result)

    def test_finalizar_compra(self):
        self.una_caja_registradora.agregar_producto(301, 0)
        self.una_caja_registradora.agregar_producto(302, 0)
        self.una_caja_registradora.agregar_producto(303, 0)
        self.una_caja_registradora.agregar_producto(304, 0)
        self.una_caja_registradora.agregar_producto(305, 0)
        result = self.una_caja_registradora.finalizar_compra()
        self.assertEqual([
            "301   Mayonesa............$  50.14",
            "302   Aceite..............$ 120.00", 
            "303   Yogurt..............$  98.35",
            "304   Café................$ 340.70",
            "305   Hamburguesas........$ 276.35",
            "TOTAL:....................$ 885.54"
        ], result)

        print("\nCÓD.  PRODUCTO              PRECIO") # comienza impresión del ticket para referencia visual
        for t in range(len(self.una_caja_registradora.ticketImpreso)):
            print(self.una_caja_registradora.ticketImpreso[t])
    
        vuelto_pago = self.una_caja_registradora.pagar_compra(900.0)
        self.assertEqual("14.46", "{0:.2f}".format(vuelto_pago))

    def test_pagar_compra_exceptions(self):
        self.una_caja_registradora.agregar_producto(301, 0)
        self.una_caja_registradora.agregar_producto(302, 0)
        self.una_caja_registradora.finalizar_compra()
        with self.assertRaises(MenorPago):
            self.una_caja_registradora.pagar_compra(50.0)

    def addCleanup(self):
        self.una_caja_registradora = []
        self.una_lista_de_precios = []

if __name__ == '__main__':
    unittest.main()

