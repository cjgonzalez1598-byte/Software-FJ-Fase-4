
class Cliente:
    """Representa un cliente del sistema."""

    def __init__(self, id_cliente, nombre, documento, telefono, correo):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono
        self.__correo = correo

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def telefono(self):
        return self.__telefono

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DEL CLIENTE ---")
        print(f"ID: {self.__id_cliente}")
        print(f"Nombre: {self.__nombre}")
        print(f"Documento: {self.__documento}")
        print(f"Teléfono: {self.__telefono}")
        print(f"Correo: {self.__correo}")

    def __str__(self):
        return f"Cliente: {self.__nombre} - Documento: {self.__documento}"
