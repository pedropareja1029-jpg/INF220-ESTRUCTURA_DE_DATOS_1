# 📋 Simulador de Lista Enlazada para Gestión de Tareas

Aplicación de escritorio y móvil desarrollada con **Python y Flet** para administrar tareas mediante una estructura de datos de tipo lista enlazada.

Este proyecto forma parte de las actividades de la asignatura **Estructuras de Datos I**, correspondiente a la Semana 3: Adaptación Multiplataforma, Visualización Avanzada y Entrega.

## 📌 Información del proyecto

- **Asignatura:** Estructuras de Datos I
- **Carrera:** Ingeniería en Sistemas
- **Universidad:** Universidad Autónoma Gabriel René Moreno (UAGRM)
- **Lenguaje:** Python
- **Framework de interfaz:** Flet
- **Plataforma móvil:** Android
- **Estado:** Aplicación funcional con APK generado y probado

## 🎯 Objetivos

- Aplicar los conceptos de listas enlazadas en un proyecto práctico.
- Desarrollar una interfaz gráfica sencilla e intuitiva.
- Implementar operaciones de creación, consulta, actualización y eliminación de tareas.
- Separar la lógica de negocio, la interfaz y el control de eventos.
- Adaptar la aplicación para su ejecución en Android.
- Documentar el funcionamiento y las posibilidades de ampliación del proyecto.

## ✨ Funcionalidades

- ➕ Agregar nuevas tareas.
- ✅ Marcar tareas como completadas.
- 🗑️ Eliminar tareas.
- 📊 Visualizar el progreso de las tareas.
- 🔄 Actualizar los indicadores de la interfaz.
- 📱 Ejecutar la aplicación en Android mediante un archivo APK.

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lógica del programa y estructuras de datos |
| Flet | Desarrollo de la interfaz gráfica |
| Flutter | Infraestructura de compilación móvil utilizada por Flet |
| Android SDK | Herramientas de compilación para Android |
| Visual Studio Code | Entorno de desarrollo |
| Git y GitHub | Control de versiones y alojamiento del código |

## 📂 Estructura del proyecto

```text
Listas_enlazadas/
├── main.py
├── Models/
│   ├── nodo.py
│   └── lista_enlazada.py
├── Views/
│   └── vista.py
├── Controller/
│   └── controlador.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Descripción de los componentes:**

- `main.py`: punto de entrada de la aplicación. Inicializa el modelo, la vista y el controlador.
- `Models/nodo.py`: define el nodo que almacena los datos y los enlaces de la estructura.
- `Models/lista_enlazada.py`: implementa la estructura de datos y las operaciones correspondientes.
- `Views/vista.py`: contiene la interfaz gráfica y los componentes visuales.
- `Controller/controlador.py`: coordina las acciones del usuario con el modelo y la vista.

## 🧠 Estructura de datos

La aplicación utiliza una lista enlazada para organizar las tareas. Cada nodo representa un elemento y mantiene una referencia al siguiente nodo de la estructura.

Esta organización permite estudiar el funcionamiento de los enlaces entre elementos y comprender cómo se realizan las operaciones sobre una colección dinámica de datos.

Las operaciones de inserción, búsqueda y eliminación pueden tener distintas complejidades según la posición del elemento y la implementación utilizada.

## ⚙️ Instalación y ejecución

### Requisitos

- Python instalado.
- Git, si se desea clonar el repositorio.
- Conexión a Internet para instalar las dependencias.

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
cd Listas_enlazadas
```

Reemplaza `URL_DE_TU_REPOSITORIO` por la dirección real del repositorio.

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python main.py
```

## 📱 Versión para Android

Se generó un archivo APK mediante Flet y las herramientas de compilación de Android.

- **Archivo:** `FletApp.apk`
- **Tamaño aproximado:** 134,1 MB
- **Estado:** compilación completada y ejecución comprobada en un dispositivo Android.

El APK podrá distribuirse mediante la sección **Releases** del repositorio o mediante un enlace externo.

> El archivo APK no se incluye directamente en el código fuente de este README. Consulta la sección Releases para obtener la versión instalable, una vez publicada.

## 🧪 Pruebas realizadas

| Prueba | Verificación |
|---|---|
| Registro de tareas | Se comprueba que una nueva tarea aparezca en la interfaz. |
| Completar tareas | Se verifica la actualización del estado y del progreso. |
| Eliminar tareas | Se comprueba que la tarea desaparezca del listado. |
| Actualización visual | Se verifica que los indicadores reflejen los cambios. |
| Ejecución en Android | Se instala y abre el APK generado. |

Las pruebas anteriores describen las verificaciones manuales realizadas durante el desarrollo. No representan una prueba automatizada ni una medición formal de rendimiento.

## 📈 Mejoras futuras

- Implementar una lista doblemente enlazada circular.
- Simular rutas de vehículos de reparto con animaciones.
- Incorporar métricas de tiempo de ejecución y consumo aproximado de memoria.
- Comparar experimentalmente operaciones O(1) y O(n).
- Guardar las tareas de forma persistente.
- Mejorar la adaptación de la interfaz a distintos tamaños de pantalla.
- Generar versiones web y para Windows.

Estas mejoras se consideran propuestas de ampliación y no funcionalidades confirmadas de la versión actual.

## 📚 Referencias

- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Flet](https://docs.flet.dev/)
- [Documentación de Flutter](https://docs.flutter.dev/)
- [Documentación de Android Developers](https://developer.android.com/)

## 👨‍💻 Autor

**Estudiante:** [Pedro Pareja Cuellar]  
**Carrera:** Ingeniería en Sistemas  
**Universidad:** Universidad Autónoma Gabriel René Moreno

Proyecto académico desarrollado con fines educativos para aplicar y demostrar conceptos de estructuras de datos mediante una interfaz gráfica multiplataforma.

