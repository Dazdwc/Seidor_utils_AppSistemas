from AppSistemas.Herramienta_Desarrollo.LicenseManager import LicenseManager
import os

if __name__ == "__main__":
    secret_key = "Beta.01_7_2024"

    # Pedir al usuario la cantidad de días de validez
    try:
        validity_period_days = int(input("Ingrese la cantidad de días de validez para el hash: "))
    except ValueError:
        print("Debe ingresar un número válido de días.")
        exit(1)

    hash_file_path = os.path.join(os.path.dirname(__file__), "hash.txt")
    license_manager = LicenseManager.LicenseManager(secret_key, validity_period_days=validity_period_days)

    hash_with_time = license_manager.generate_timed_hash()
    print(f"Hash generado: {hash_with_time}")

    # Guardar el hash en un archivo
    with open(hash_file_path, "w") as file:
        file.write(hash_with_time)
    print(f"Hash guardado en {hash_file_path}")