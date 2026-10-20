
class Controlador:
    """Conecta la vista con el modelo."""

    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.controlador = self

        self.mostrar_tareas()

    def agregar_tarea(self):
        datos = self.vista.obtener_tarea().strip()

        if not datos:
            self.vista.mostrar_mensaje(
                "Escribe una tarea antes de agregarla."
            )
            return

        self.modelo.agregar_tarea(datos)
        self.vista.limpiar_entrada()
        self.vista.mostrar_mensaje("Tarea agregada.")
        self.mostrar_tareas()

    def completar_tarea(self, datos):
        resultado = self.modelo.completar_tarea(datos)

        if resultado:
            self.vista.mostrar_mensaje("Tarea completada.")
        else:
            self.vista.mostrar_mensaje(
                "No se encontró la tarea."
            )

        self.mostrar_tareas()

    def eliminar_tarea(self, datos):
        resultado = self.modelo.eliminar_tarea(datos)

        if resultado:
            self.vista.mostrar_mensaje("Tarea eliminada.")
        else:
            self.vista.mostrar_mensaje(
                "No se encontró la tarea."
            )

        self.mostrar_tareas()

    def mostrar_tareas(self):
        tareas = self.modelo.obtener_tareas()
        self.vista.mostrar_tareas(tareas)
