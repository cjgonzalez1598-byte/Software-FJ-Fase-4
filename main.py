from gestor import GestorSistema
from clientes import Cliente
from servicios import ReservaSala
from reservas import Reserva
print("=" * 55)
print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
print(" Clientes, Servicios y Reservas")
print("=" * 55)

print("\nBienvenido al sistema Software FJ")
print("Inicializando aplicacion...")
print("\nSistema iniciado correctamente.")

print("\nConectando módulos del sistema...")

sistema = GestorSistema()
# Registrar un cliente de prueba
nuevo_cliente = Cliente(
    "CLI001",
    "Juan Perez",
    "123456789",
    "3001234567",
    "juan@gmail.com"
)

sistema.registrar_cliente(nuevo_cliente)
# Registrar un servicio de prueba
nuevo_servicio = ReservaSala(
    "SER001",
    "Sala principal",
    "Sala para reuniones y eventos",
    50000,
    20,
    25000
)

sistema.registrar_servicio(nuevo_servicio)
# Registrar una reserva de prueba
sistema.crear_reserva(
    "RES001",
    "CLI001",
    "SER001",
    cantidad=1,
    observaciones="Reserva de prueba"
)
# ==========================================
# PRUEBAS DEL SISTEMA - 10 OPERACIONES
# ==========================================

print("\n========== INICIO DE LAS 10 PRUEBAS ==========")

def ejecutar_prueba(numero, descripcion, accion, error_esperado=None):
    try:
        accion()

        if error_esperado:
            print(f"PRUEBA {numero}: FALLIDA - No se produjo el error esperado.")
        else:
            print(f"PRUEBA {numero}: EXITOSA - {descripcion}")

    except Exception as error:
        if error_esperado and isinstance(error, error_esperado):
            print(f"PRUEBA {numero}: EXITOSA - {descripcion}")
        else:
            print(f"PRUEBA {numero}: FALLIDA - {error}")


# PRUEBA 1: Buscar cliente existente
ejecutar_prueba(
    1,
    "Busqueda de cliente existente",
    lambda: sistema.buscar_cliente("CLI001")
)

# PRUEBA 2: Evitar registrar clientes duplicados
ejecutar_prueba(
    2,
    "Control de clientes duplicados",
    lambda: sistema.registrar_cliente(nuevo_cliente),
    ValueError
)

# PRUEBA 3: Buscar cliente inexistente
ejecutar_prueba(
    3,
    "Control de cliente inexistente",
    lambda: sistema.buscar_cliente("CLI999"),
    ValueError
)

# PRUEBA 4: Buscar servicio existente
ejecutar_prueba(
    4,
    "Busqueda de servicio existente",
    lambda: sistema.buscar_servicio("SER001")
)

# PRUEBA 5: Evitar servicios duplicados
ejecutar_prueba(
    5,
    "Control de servicios duplicados",
    lambda: sistema.registrar_servicio(nuevo_servicio),
    ValueError
)

# PRUEBA 6: Buscar servicio inexistente
ejecutar_prueba(
    6,
    "Control de servicio inexistente",
    lambda: sistema.buscar_servicio("SER999"),
    ValueError
)

# PRUEBA 7: Crear una segunda reserva correctamente
ejecutar_prueba(
    7,
    "Creacion de una nueva reserva",
    lambda: sistema.crear_reserva(
        "RES002",
        "CLI001",
        "SER001",
        cantidad=1,
        observaciones="Segunda reserva de prueba"
    )
)

# PRUEBA 8: Cancelar una reserva
ejecutar_prueba(
    8,
    "Cancelacion de reserva",
    lambda: sistema.cancelar_reserva("RES002")
)

# PRUEBA 9: Crear reserva con cliente inexistente
ejecutar_prueba(
    9,
    "Control de reserva con cliente inexistente",
    lambda: sistema.crear_reserva(
        "RES003",
        "CLI999",
        "SER001"
    ),
    ValueError
)

# PRUEBA 10: Evitar reservas duplicadas
ejecutar_prueba(
    10,
    "Control de reservas duplicadas",
    lambda: sistema.crear_reserva(
        "RES001",
        "CLI001",
        "SER001"
    ),
    ValueError
)

print("\n========== FINALIZACION DE LAS PRUEBAS ==========\n")
sistema.listar_reservas()
sistema.mostrar_resumen()