from .estudiante import devolver_materias
from typing import List

def estudiante_registrado_en_materia(nombre_estudiante: str, materia: str) -> bool:
    """
    Determina si un estudiante está registrado en una materia.
    
    :param nombre_estudiante: Nombre del estudiante.
    :param materia: Nombre de la materia.
    :return: True si el estudiante está registrado en la materia, False en caso contrario.
    """
    try:
        materias: List[str] = devolver_materias(nombre_estudiante)
        return materia in materias
    except Exception as e:
        print(f"Detalle del error: {e}")
        return False
