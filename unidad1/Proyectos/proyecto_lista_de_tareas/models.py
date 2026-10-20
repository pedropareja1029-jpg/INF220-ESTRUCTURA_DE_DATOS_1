
from Models.nodo import Nodo


class ListaEnlazada:
    """Implementa una lista enlazada de tareas."""

    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, datos):
        """Agrega una tarea al final de la lista."""
        nuevo_nodo = Nodo(datos)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def completar_tarea(self, datos):
        """Marca una tarea como completada."""
        actual = self.cabeza

        while actual is not None:
            if actual.datos == datos:
                actual.estado = "completada"
                return True

            actual = actual.siguiente

        return False

    def eliminar_tarea(self, datos):
        """Elimina la primera tarea que coincida."""
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.datos == datos:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def obtener_tareas(self):
        """Devuelve las tareas con sus estados."""
        tareas = []
        actual = self.cabeza

        while actual is not None:
            tareas.append(
                f"{actual.datos} - {actual.estado}"
            )
            actual = actual.siguiente

        return tareas

