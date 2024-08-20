from Herramienta_Desarrollo.controladores.MainController import MainController
from Herramienta_Desarrollo.LicenseManager import LicenseManager
from Herramienta_Desarrollo.vista.Vista import show_error_message
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    # Configuración del LicenseManager
    secret_key = "Beta.02_7_2024"
    # Asegurarse de que la ruta al hash.txt es correcta
    hash_file_path = resource_path("hash.txt")
    license_manager = LicenseManager.LicenseManager(secret_key, hash_file_path=hash_file_path)

    # Verificar la licencia
    if license_manager.check_license():
        print("Clave válida. Iniciando la aplicación...")
        controller = MainController()
        controller.run()
    else:
        show_error_message(f"No se pudo verificar la licencia. Por favor, contacte al soporte. Error: {hash_file_path}, {secret_key}")
        print("No se pudo verificar la licencia. La aplicación no se iniciará.")