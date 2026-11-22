
from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):
    """Clase abstracta que representa un servicio del sistema."""

    def __init__(self, id_servicio, nombre, descripcion, precio_base):
        self.__id_servicio = id_servicio
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_base = precio_base
        self.__disponible = True

    @property
    def id_servicio(self):
        return self.__id_servicio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_base(self):
        return self.__precio_base

    @property
    def disponible(self):
        return self.__disponible

    def verificar_disponibilidad(self):
        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.__nombre} no está disponible."
            )
        return True

    def cambiar_disponibilidad(self, estado):
        self.__disponible = estado

    @abstractmethod
    def calcular_costo(self, cantidad=1):
        """Calcula el costo según el tipo de servicio."""
        pass

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DEL SERVICIO ---")
        print(f"ID: {self.__id_servicio}")
        print(f"Nombre: {self.__nombre}")
        print(f"Descripción: {self.__descripcion}")
        print(f"Precio base: ${self.__precio_base:,.2f}")
        print(f"Disponible: {'Sí' if self.__disponible else 'No'}")

    def __str__(self):
        return f"Servicio: {self.__nombre} - ID: {self.__id_servicio}"


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, id_servicio, nombre, descripcion,
                 precio_base, capacidad, costo_hora):
        super().__init__(id_servicio, nombre, descripcion, precio_base)
        self.__capacidad = capacidad
        self.__costo_hora = costo_hora

    @property
    def capacidad(self):
        return self.__capacidad

    def calcular_costo(self, cantidad=1):
        self.verificar_disponibilidad()
        return self.__costo_hora * cantidad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de la sala: {self.__capacidad} personas")
        print(f"Costo por hora: ${self.__costo_hora:,.2f}")


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def __init__(self, id_servicio, nombre, descripcion,
                 precio_base, tipo_equipo, costo_dia):
        super().__init__(id_servicio, nombre, descripcion, precio_base)
        self.__tipo_equipo = tipo_equipo
        self.__costo_dia = costo_dia

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    def calcular_costo(self, cantidad=1):
        self.verificar_disponibilidad()
        return self.__costo_dia * cantidad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de equipo: {self.__tipo_equipo}")
        print(f"Costo por día: ${self.__costo_dia:,.2f}")


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorías especializadas."""

    def __init__(self, id_servicio, nombre, descripcion,
                 precio_base, especialidad, costo_hora):
        super().__init__(id_servicio, nombre, descripcion, precio_base)
        self.__especialidad = especialidad
        self.__costo_hora = costo_hora

    @property
    def especialidad(self):
        return self.__especialidad

    def calcular_costo(self, cantidad=1):
        self.verificar_disponibilidad()
        return self.__costo_hora * cantidad

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self.__especialidad}")
        print(f"Costo por hora: ${self.__costo_hora:,.2f}")
