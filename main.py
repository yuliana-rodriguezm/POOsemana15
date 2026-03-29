from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():

    # Crear el servicio (lógica del sistema)
    servicio = TareaServicio()

    # Crear la aplicación gráfica
    app = AppTkinter(servicio)

    # Ejecutar la aplicación
    app.mainloop()


if __name__ == "__main__":
    main()