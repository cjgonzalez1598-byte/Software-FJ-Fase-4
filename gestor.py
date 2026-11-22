
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva, GestorReservas


class GestorSistema:
    """Administra las operaciones generales del Software FJ."""

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__gestor_reservas = GestorReservas()

    @property
    def clientes(self):
        return self.__clientes.copy()

    @property
    def servicios(self):
        return self.__servicios.copy()

    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente."""

        if not isinstance(cliente, Cliente):
            raise TypeError("Debe ingresar un cliente válido.")

        for existente in self.__clientes:
            if existente.id_cliente == cliente.id_cliente:
                raise ValueError("El cliente ya se encuentra registrado.")

        self.__clientes.append(cliente)
        print("Cliente registrado correctamente.")
        return True

    def buscar_cliente(self, id_cliente):
        """Busca un cliente por su identificación."""

        for cliente in self.__clientes:
            if cliente.id_cliente == id_cliente:
                return cliente

        raise ValueError("No se encontró el cliente solicitado.")

    def listar_clientes(self):
        """Muestra los clientes registrados."""

        print("\n========== LISTADO DE CLIENTES ==========")

        if not self.__clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self.__clientes:
            print(cliente)

    def registrar_servicio(self, servicio):
        """Registra un nuevo servicio."""

        if not isinstance(servicio, Servicio):
            raise TypeError("Debe ingresar un servicio válido.")

        for existente in self.__servicios:
            if existente.id_servicio == servicio.id_servicio:
                raise ValueError("El servicio ya se encuentra registrado.")

        self.__servicios.append(servicio)
        print("Servicio registrado correctamente.")
        return True

    def buscar_servicio(self, id_servicio):
        """Busca un servicio por su identificador."""

        for servicio in self.__servicios:
            if servicio.id_servicio == id_servicio:
                return servicio

        raise ValueError("No se encontró el servicio solicitado.")

    def listar_servicios(self):
        """Muestra los servicios disponibles."""

        print("\n========== LISTADO DE SERVICIOS ==========")

        if not self.__servicios:
            print("No hay servicios registrados.")
            return

        for servicio in self.__servicios:
            servicio.mostrar_informacion()

    def crear_reserva(self, id_reserva, id_cliente,
                      id_servicio, cantidad=1,
                      observaciones=""):
        """Crea y registra una reserva."""

        cliente = self.buscar_cliente(id_cliente)
        servicio = self.buscar_servicio(id_servicio)

        reserva = Reserva(
            id_reserva,
            cliente,
            servicio,
            cantidad,
            observaciones
        )

        self.__gestor_reservas.registrar_reserva(reserva)

        print("Reserva creada correctamente.")
        return reserva

    def listar_reservas(self):
        """Muestra todas las reservas."""

        self.__gestor_reservas.listar_reservas()

    def buscar_reserva(self, id_reserva):
        """Busca una reserva registrada."""

        return self.__gestor_reservas.buscar_reserva(id_reserva)

    def cancelar_reserva(self, id_reserva):
        """Cancela una reserva."""

        return self.__gestor_reservas.cancelar_reserva(id_reserva)

    def mostrar_resumen(self):
        """Muestra un resumen general del sistema."""

        print("\n========== RESUMEN DEL SOFTWARE FJ ==========")
        print(f"Clientes registrados: {len(self.__clientes)}")
        print(f"Servicios registrados: {len(self.__servicios)}")
        print(
            f"Reservas registradas: "
            f"{self.__gestor_reservas.contar_reservas()}"
        )

        self.__gestor_reservas.mostrar_resumen()

        print("=============================================")
