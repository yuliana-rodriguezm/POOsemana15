from modelos.tarea import Tarea
from typing import List, Optional


class TareaServicio:

    def __init__(self):
        # Lista interna donde se almacenan las tareas
        self._lista_tareas: List[Tarea] = []
        self._siguiente_id = 1


    def agregar_tarea(self, tarea: Tarea) -> None:
        # Agrega una nueva tarea al sistema
        self._lista_tareas.append(tarea)
        self._siguiente_id += 1


    def obtener_siguiente_id(self) -> int:
        return self._siguiente_id

    def obtener_todas(self) -> List[Tarea]:
        # Retorna todas las tareas registradas
        return self._lista_tareas


    def completar_tarea(self, id_tarea: int) -> None:
        # Cambia el estado de una tarea a completada
        tarea = self._buscar_tarea(id_tarea)

        if tarea is None:
            raise ValueError("No se encontró la tarea indicada.")

        tarea.completada = True


    def eliminar_tarea(self, id_tarea: int) -> None:

        #Elimina una tarea existente
        tarea = self._buscar_tarea(id_tarea)

        if tarea is None:
            raise ValueError("No existe la tarea que intenta eliminar.")

        self._lista_tareas.remove(tarea)


    def _buscar_tarea(self, id_tarea: int) -> Optional[Tarea]:
       # Método auxiliar para localizar una tarea por su ID
        for tarea in self._lista_tareas:
            if tarea.id == id_tarea:
                return tarea

        return None