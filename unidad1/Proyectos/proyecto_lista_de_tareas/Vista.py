import flet as ft


class Vista:
    """Interfaz gráfica roja y blanca para la lista de tareas."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.controlador = None

        # Colores de la aplicación
        self.rojo = "#D62839"
        self.rojo_claro = "#FCE8EA"
        self.fondo = "#F7F7F9"
        self.texto = "#252535"
        self.gris = "#858594"
        self.verde = "#21875A"

        # Campo para escribir tareas
        self.entrada = ft.TextField(
            hint_text="¿Qué necesitas hacer?",
            expand=True,
            border_radius=12,
            bgcolor="#FFFFFF",
            border_color="#E5E5EB",
            focused_border_color=self.rojo,
            text_size=14,
        )

        # Mensajes para el usuario
        self.mensaje = ft.Text(
            size=13,
            color=self.rojo,
        )

        # Lista visual
        self.lista = ft.Column(spacing=10)

        # Contadores
        self.total_texto = ft.Text(
            "0 tareas",
            size=13,
            color=self.gris,
        )

        self.progreso_texto = ft.Text(
            "0% completado",
            size=12,
            color="#FFFFFF",
        )

        self.progreso_barra = ft.ProgressBar(
            value=0,
            color="#FFFFFF",
            bgcolor="#A83A45",
            bar_height=7,
        )

        # Configuración de la ventana
        self.page.title = "Mis tareas"
        self.page.padding = 20
        self.page.bgcolor = self.fondo
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.scroll = ft.ScrollMode.AUTO

        # Encabezado
        encabezado = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    spacing=4,
                    controls=[
                        ft.Text(
                            "MI ESPACIO PERSONAL",
                            size=10,
                            color=self.rojo,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Mis tareas",
                            size=30,
                            color=self.texto,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Organiza tu día, paso a paso.",
                            size=13,
                            color=self.gris,
                        ),
                    ],
                ),
                ft.Container(
                    content=ft.Icon(
                        icon=ft.Icons.CHECK_CIRCLE,
                        color=self.rojo,
                        size=32,
                    ),
                    bgcolor=self.rojo_claro,
                    padding=12,
                    border_radius=15,
                ),
            ],
        )

        # Tarjeta de progreso
        tarjeta_progreso = ft.Container(
            content=ft.Column(
                spacing=12,
                controls=[
                    ft.Text(
                        "Tu progreso",
                        size=14,
                        color="#FFFFFF",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "¡Tú puedes!",
                                size=22,
                                color="#FFFFFF",
                                weight=ft.FontWeight.BOLD,
                            ),
                            self.progreso_texto,
                        ],
                    ),
                    self.progreso_barra,
                ],
            ),
            bgcolor=self.rojo,
            padding=20,
            border_radius=18,
        )

        # Campo para agregar tareas
        seccion_nueva = ft.Column(
            spacing=10,
            controls=[
                ft.Text(
                    "Nueva tarea",
                    size=18,
                    color=self.texto,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(
                    spacing=8,
                    controls=[
                        self.entrada,
                        ft.IconButton(
                            icon=ft.Icons.ADD_CIRCLE,
                            icon_color=self.rojo,
                            icon_size=38,
                            tooltip="Agregar tarea",
                            on_click=self._agregar,
                        ),
                    ],
                ),
                self.mensaje,
            ],
        )

        # Encabezado de la lista
        encabezado_lista = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    "Lista de tareas",
                    size=18,
                    color=self.texto,
                    weight=ft.FontWeight.BOLD,
                ),
                self.total_texto,
            ],
        )

        # Contenido principal
        self.page.add(
            ft.Column(
                spacing=18,
                controls=[
                    encabezado,
                    tarjeta_progreso,
                    seccion_nueva,
                    encabezado_lista,
                    self.lista,
                ],
            )
        )

    def _agregar(self, e):
        """Solicita agregar una tarea al controlador."""
        if self.controlador:
            self.controlador.agregar_tarea()

    def obtener_tarea(self):
        """Devuelve el texto introducido."""
        return self.entrada.value or ""

    def limpiar_entrada(self):
        """Vacía el campo de entrada."""
        self.entrada.value = ""

    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje al usuario."""
        self.mensaje.value = mensaje
        self.page.update()

    def mostrar_tareas(self, tareas):
        """Actualiza la lista, los contadores y el progreso."""

        self.lista.controls.clear()

        total = len(tareas)
        completadas = sum(
            1
            for tarea in tareas
            if tarea.endswith("- completada")
        )

        porcentaje = completadas / total if total else 0

        # Actualizar contador y progreso
        self.total_texto.value = (
            "1 tarea" if total == 1 else f"{total} tareas"
        )

        self.progreso_texto.value = (
            f"{round(porcentaje * 100)}% completado"
        )

        self.progreso_barra.value = porcentaje

        # Mostrar mensaje cuando la lista está vacía
        if not tareas:
            self.lista.controls.append(
                ft.Container(
                    content=ft.Column(
                        horizontal_alignment=(
                            ft.CrossAxisAlignment.CENTER
                        ),
                        spacing=8,
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.EVENT_NOTE,
                                color=self.rojo,
                                size=42,
                            ),
                            ft.Text(
                                "Todavía no tienes tareas",
                                size=16,
                                color=self.texto,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                "Agrega tu primera tarea arriba.",
                                size=13,
                                color=self.gris,
                            ),
                        ],
                    ),
                    bgcolor="#FFFFFF",
                    padding=25,
                    border_radius=16,
                )
            )

        else:
            # Crear una tarjeta por cada tarea
            for tarea in tareas:
                completada = tarea.endswith("- completada")
                texto = tarea.rsplit(" - ", 1)[0]

                tarjeta = ft.Container(
                    content=ft.Row(
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                icon=(
                                    ft.Icons.CHECK_CIRCLE
                                    if completada
                                    else ft.Icons.RADIO_BUTTON_UNCHECKED
                                ),
                                color=(
                                    self.verde
                                    if completada
                                    else self.rojo
                                ),
                                size=23,
                            ),
                            ft.Column(
                                spacing=4,
                                expand=True,
                                controls=[
                                    ft.Text(
                                        texto,
                                        size=14,
                                        color=(
                                            self.gris
                                            if completada
                                            else self.texto
                                        ),
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                    ft.Text(
                                        (
                                            "Completada"
                                            if completada
                                            else "Pendiente"
                                        ),
                                        size=11,
                                        color=(
                                            self.verde
                                            if completada
                                            else self.gris
                                        ),
                                    ),
                                ],
                            ),
                            ft.IconButton(
                                icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                                icon_color=self.verde,
                                tooltip="Completar tarea",
                                disabled=completada,
                                on_click=lambda e, t=texto: (
                                    self.controlador.completar_tarea(t)
                                ),
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=self.rojo,
                                tooltip="Eliminar tarea",
                                on_click=lambda e, t=texto: (
                                    self.controlador.eliminar_tarea(t)
                                ),
                            ),
                        ],
                    ),
                    bgcolor="#FFFFFF",
                    padding=10,
                    border_radius=14,
                )

                self.lista.controls.append(tarjeta)

        self.page.update()

