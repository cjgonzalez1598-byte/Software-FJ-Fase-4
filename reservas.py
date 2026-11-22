
from datetime import datetime
import logging

from excepciones import (
    ReservaNoEncontradaError,
    ReservaDuplicadaError,
    ServicioNoDisponibleError
)


logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class Reserva:
    """Representa una reserva realizada por un cliente."""

    def __init__(self, id_reserva, cliente, servicio,
                 cantidad=1, observaciones=""):

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__cantidad = cantidad
        self.__observaciones = observaciones
        self.__fecha = datetime.now()
        self.__estado = "Activa"

        logging.info(f"Reserva {id_reserva} creada.")

    @property
    def id_reserva(self):
        return self.__id_reserva

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def fecha(self):
        return self.__fecha

    @property
    def estado(self):
        return self.__estado

    @property
    def observaciones(self):
        return self.__observaciones

    def calcular_total(self):
        """Calcula el valor total de la reserva."""

        if self.__estado != "Activa":
            raise ValueError("La reserva no está activa.")

        return self.__servicio.calcular_costo(self.__cantidad)

    def cancelar(self):
        """Cancela una reserva activa."""

        if self.__estado != "Activa":
            raise ValueError("La reserva ya fue cancelada.")

        self.__estado = "Cancelada"

        logging.info(
            f"Reserva {self.__id_reserva} cancelada."
        )

    def modificar_cantidad(self, nueva_cantidad):
        """Modifica la cantidad de horas o días reservados."""

        if not isinstance(nueva_cantidad, (int, float)):
            raise ValueError("La cantidad debe ser numérica.")

        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if self.__estado != "Activa":
            raise ValueError("No se puede modificar una reserva cancelada.")

        self.__cantidad = nueva_cantidad

        logging.info(
            f"Cantidad de reserva {self.__id_reserva} modificada."
        )

    def mostrar_informacion(self):
        """Muestra los datos completos de la reserva."""

        print("\n========== INFORMACIÓN DE LA RESERVA ==========")
        print(f"ID de reserva: {self.__id_reserva}")
        print(f"Cliente: {self.__cliente.nombre}")
        print(f"Servicio: {self.__servicio.nombre}")
        print(f"Cantidad: {self.__cantidad}")
        print(f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}")
        print(f"Estado: {self.__estado}")
        print(f"Observaciones: {self.__observaciones}")

        if self.__estado == "Activa":
            try:
                total = self.calcular_total()
                print(f"Valor total: ${total:,.2f}")
            except ServicioNoDisponibleError as error:
                print(f"No se puede calcular el valor: {error}")

        print("===============================================")

    def __str__(self):
        return (
            f"Reserva: {self.__id_reserva} - "
            f"Cliente: {self.__cliente.nombre} - "
            f"Estado: {self.__estado}"
        )


class GestorReservas:
    """Administra las reservas del sistema Software FJ."""

    def __init__(self):
        self.__reservas = []

    def registrar_reserva(self, reserva):
        """Registra una nueva reserva."""

        if not isinstance(reserva, Reserva):
            raise TypeError("El objeto debe ser una reserva válida.")

        for existente in self.__reservas:
            if existente.id_reserva == reserva.id_reserva:
                raise ReservaDuplicadaError(
                    f"La reserva {reserva.id_reserva} ya existe."
                )

        reserva.servicio.verificar_disponibilidad()

        self.__reservas.append(reserva)

        logging.info(
            f"Reserva {reserva.id_reserva} registrada correctamente."
        )

        return True

    def buscar_reserva(self, id_reserva):
        """Busca una reserva por su identificador."""

        for reserva in self.__reservas:
            if reserva.id_reserva == id_reserva:
                return reserva

        raise ReservaNoEncontradaError(
            f"No se encontró la reserva {id_reserva}."
        )

    def eliminar_reserva(self, id_reserva):
        """Elimina una reserva del registro."""

        reserva = self.buscar_reserva(id_reserva)

        self.__reservas.remove(reserva)

        logging.info(f"Reserva {id_reserva} eliminada.")

        return True

    def cancelar_reserva(self, id_reserva):
        """Cancela una reserva registrada."""

        reserva = self.buscar_reserva(id_reserva)
        reserva.cancelar()

        return True

    def listar_reservas(self):
        """Muestra todas las reservas registradas."""

        if not self.__reservas:
            print("No hay reservas registradas.")
            return

        print("\n========== LISTADO DE RESERVAS ==========")

        for reserva in self.__reservas:
            print(reserva)

        print("=========================================")

    def buscar_reservas_cliente(self, id_cliente):
        """Consulta las reservas de un cliente."""

        resultados = []

        for reserva in self.__reservas:
            if reserva.cliente.id_cliente == id_cliente:
                resultados.append(reserva)

        return resultados

    def contar_reservas(self):
        """Devuelve la cantidad de reservas registradas."""

        return len(self.__reservas)

    def calcular_ingresos(self):
        """Calcula el total de las reservas activas."""

        total = 0

        for reserva in self.__reservas:
            if reserva.estado == "Activa":
                try:
                    total += reserva.calcular_total()
                except ServicioNoDisponibleError as error:
                    logging.warning(str(error))

        return total

    def mostrar_resumen(self):
        """Muestra un resumen general de las reservas."""

        print("\n========== RESUMEN DE RESERVAS ==========")
        print(f"Total de reservas: {self.contar_reservas()}")
        print(f"Ingresos estimados: ${self.calcular_ingresos():,.2f}")
        print("=========================================")
