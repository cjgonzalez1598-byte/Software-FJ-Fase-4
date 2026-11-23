# Excepciones personalizadas del sistema Software FJ

class ErrorSistema(Exception):
    """Error general del sistema."""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error cuando los datos del cliente no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaNoEncontradaError(ErrorSistema):
    """Error cuando no se encuentra una reserva."""
    pass


class ReservaDuplicadaError(ErrorSistema):
    """Error cuando una reserva ya existe."""
    pass
