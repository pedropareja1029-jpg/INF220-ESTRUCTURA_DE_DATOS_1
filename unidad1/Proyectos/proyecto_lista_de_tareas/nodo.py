
class Nodo:
    """Representa una tarea de la lista enlazada."""

    def __init__(self, datos):
        self.datos = datos
        self.estado = "pendiente"
        self.siguiente = None

