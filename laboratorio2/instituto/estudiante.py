from typing import List

# Diccionario de estudiantes y sus materias
estudiantes_materias: dict[str, List[str]] = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def devolver_materias(nombre_estudiante: str) -> List[str]:
    """
    Devuelve la lista de materias para un estudiante dado.
    
    :param nombre_estudiante: Nombre del estudiante.
    :return: Lista de materias del estudiante.
    :raises Exception: Si el estudiante no está registrado.
    """
    try:
        return estudiantes_materias[nombre_estudiante]
    except KeyError:
        raise Exception(f"El estudiante {nombre_estudiante} no está registrado.")
