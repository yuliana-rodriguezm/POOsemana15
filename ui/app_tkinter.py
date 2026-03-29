import tkinter as tk
from tkinter import messagebox
from modelos.tarea import Tarea


class AppTkinter(tk.Tk):

    def __init__(self, servicio):
        super().__init__()

        self.servicio = servicio
        self._id_seleccionado = None

        self.title("Lista de Tareas")
        self.geometry("500x400")

        self._configurar_interfaz()
        self._registrar_eventos()


    # INTERFAZ
    def _configurar_interfaz(self):

        frame_top = tk.Frame(self)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Nueva tarea:").pack(side=tk.LEFT)

        self.entry_tarea = tk.Entry(frame_top, width=30)
        self.entry_tarea.pack(side=tk.LEFT, padx=5)

        btn_agregar = tk.Button(
            frame_top,
            text="Añadir Tarea",
            command=self._agregar_tarea
        )
        btn_agregar.pack(side=tk.LEFT)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        btn_completar = tk.Button(
            frame_botones,
            text="Marcar Completada",
            command=self._completar_tarea
        )
        btn_completar.pack(side=tk.LEFT, padx=5)

        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            command=self._eliminar_tarea
        )
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # LISTA DE TAREAS
        self.lista = tk.Listbox(self, width=60, height=15)
        self.lista.pack(pady=10)


    # EVENTOS
    def _registrar_eventos(self):

        # Enter para agregar tarea
        self.entry_tarea.bind("<Return>", self._evento_enter)

        # Seleccionar tarea
        self.lista.bind("<<ListboxSelect>>", self._seleccionar_tarea)

        # Doble clic para completar tarea
        self.lista.bind("<Double-1>", self._evento_doble_click)

    def _evento_enter(self, event):
        self._agregar_tarea()

    def _evento_doble_click(self, event):
        self._completar_tarea()


    # FUNCIONES PRINCIPALES
    def _agregar_tarea(self):

        descripcion = self.entry_tarea.get().strip()

        if not descripcion:
            messagebox.showwarning("Atención", "Debe escribir una tarea")
            return

        try:
            id_tarea = self.servicio.obtener_siguiente_id()
            tarea = Tarea(id_tarea, descripcion)

            self.servicio.agregar_tarea(tarea)

            self._actualizar_lista()
            self.entry_tarea.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _completar_tarea(self):

        if self._id_seleccionado is None:
            messagebox.showwarning("Atención", "Seleccione una tarea")
            return

        try:
            self.servicio.completar_tarea(self._id_seleccionado)
            self._actualizar_lista()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_tarea(self):

        if self._id_seleccionado is None:
            messagebox.showwarning("Atención", "Seleccione una tarea")
            return

        try:
            self.servicio.eliminar_tarea(self._id_seleccionado)
            self._actualizar_lista()
            self._id_seleccionado = None

        except ValueError as e:
            messagebox.showerror("Error", str(e))


    # ACTUALIZAR LISTA
    def _actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for tarea in self.servicio.obtener_todas():

            texto = tarea.descripcion

            if tarea.completada:
                texto = "✔ " + texto

            self.lista.insert(tk.END, f"{tarea.id} - {texto}")

    def _seleccionar_tarea(self, event):

        seleccion = self.lista.curselection()

        if seleccion:
            indice = seleccion[0]
            tarea = self.servicio.obtener_todas()[indice]

            self._id_seleccionado = tarea.id