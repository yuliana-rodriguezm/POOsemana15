# Lista de Tareas - Aplicación GUI con Tkinter

## Descripción

Este proyecto consiste en el desarrollo de una aplicación de escritorio para la gestión de tareas (To-Do List), creada utilizando Python y la librería Tkinter.

La aplicación permite al usuario agregar, completar y eliminar tareas mediante una interfaz gráfica interactiva. Además, se implementa el manejo de eventos de teclado y ratón para mejorar la experiencia del usuario.

El proyecto fue desarrollado respetando una arquitectura modular por capas, separando claramente el modelo de datos, la lógica del negocio y la interfaz gráfica.

## Funcionalidades

La aplicación permite realizar las siguientes acciones:

* Agregar tareas

El usuario puede escribir una tarea en el campo de entrada y presionar el botón Añadir Tarea o la tecla Enter.

* Marcar tareas como completadas

Las tareas seleccionadas pueden marcarse como completadas mediante el botón correspondiente o con doble clic.

* Eliminar tareas

Las tareas seleccionadas pueden eliminarse de la lista.

* Feedback visual

Cuando una tarea se marca como completada, su apariencia cambia para indicar su estado.

# Manejo de Eventos

Se implementaron diferentes eventos para interactuar con la aplicación:

* Evento de teclado

Presionar Enter permite agregar una nueva tarea.

* Evento de ratón

Doble clic sobre una tarea permite marcarla como completada.

## Tecnologías utilizadas

* Python 3
* Tkinter (biblioteca estándar para interfaces gráficas)
* PyInstaller para generar el archivo ejecutable
* GitHub para el repositorio del proyecto


## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

* **main.py**

* Archivo principal que actúa como punto de inicio de la aplicación y conecta los servicios con la interfaz gráfica.

* **modelos/**
* Contiene las clases que representan las entidades del sistema.

tarea.py: define la clase Tarea, con atributos como:
id
descripcion
estado de completado

* **servicios/**
* Contiene la lógica del negocio de la aplicación.

tarea_servicio.py: permite
agregar tareas
marcar tareas como completadas
eliminar tareas
listar tareas

* **ui/**
* Contiene la interfaz gráfica de usuario.

app_tkinter.py: implementación de la interfaz usando Tkinter, incluyendo botones, campo de entrada y lista de tareas.

## Generación del Ejecutable

Para generar el archivo ejecutable se utilizó PyInstaller con el siguiente comando:

```
pyinstaller --noconsole --onefile --name ListaTareas main.py
```

Esto genera el archivo .exe dentro de la carpeta:

dist/

El ejecutable permite utilizar la aplicación sin necesidad de tener Python instalado.

## Ejecución del programa

1. Descargar o clonar el repositorio.
2. Ejecutar el archivo principal:

```
python main.py
```

Se abrirá la ventana del sistema de registro de visitantes.


## Nota

Durante el proceso de empaquetado de la aplicación con PyInstaller se generaron carpetas y archivos temporales como build/, dist/ y archivos .spec.

Inicialmente estos archivos aparecieron en el repositorio, pero posteriormente fueron excluidos correctamente mediante el archivo .gitignore, ya que corresponden a archivos generados automáticamente durante la compilación del ejecutable y no forman parte del código fuente del proyecto.
