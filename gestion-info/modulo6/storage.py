import json

ARCHIVO = "usuarios.json"


def cargar_datos() -> list:
    """
    Carga usuarios desde un archivo JSON.
    """
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_datos(usuarios: list) -> None:
    """
    Guarda usuarios en un archivo JSON.
    """
    with open(ARCHIVO, "w") as f:
        json.dump(usuarios, f, indent=4)