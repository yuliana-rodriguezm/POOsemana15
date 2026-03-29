class Tarea:

    def __init__(self, identificador: int, descripcion: str):
        # Usamos propiedades para aplicar validaciones
        self.id = identificador
        self.descripcion = descripcion
        self.completada = False


    # IDENTIFICADOR

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, valor: int):
        if valor <= 0:
            raise ValueError("El identificador de la tarea debe ser mayor que cero.")
        self._id = valor

  
    # DESCRIPCIÓN

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, texto: str):
        if not texto or not texto.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía.")
        self._descripcion = texto.strip()


    # ESTADO DE LA TAREA

    @property
    def completada(self) -> bool:
        return self._completada

    @completada.setter
    def completada(self, valor: bool):
        self._completada = valor