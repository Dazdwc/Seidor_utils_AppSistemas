---

# License Manager 🔐📜

## Descripción 📄🛠️

El License Manager es una herramienta que permite validar las licencias generadas mediante el hash. Se encarga de verificar si una licencia es válida o ha expirado, asegurando que el software solo pueda ser usado por usuarios con acceso autorizado.

### Generar un hash de licencia
Ejecuta el script del generador de hashes:
```sh
python generate_hash.py
```
Se solicitará la cantidad de días de validez y se generará un hash en `hash.txt`.

### Verificar una licencia
Ejecuta el License Manager:
```sh
python license_manager.py
```
El programa verificará si el hash almacenado en `hash.txt` es válido o ha expirado.

## ¿Por qué son necesarias ambas herramientas? 🤔🔍

El Generador de Hashes permite establecer licencias temporales para controlar el acceso a un software. Sin embargo, para asegurar que estas licencias sean respetadas, el License Manager se encarga de validar cada hash generado y determinar si sigue vigente o ha caducado.

---

## Estructura del Proyecto 📂🗂️
```
/
├── generate_hash.py  # Generador de hashes
├── license_manager.py  # Gestor de licencias
├── hash.txt  # Archivo donde se almacena el hash generado
└── Herramienta_Desarrollo/
    ├── LicenseManager.py  # Clase para manejar licencias
```

## Notas 📌🔍
- La clave secreta está definida en el código y debe mantenerse segura.
- Si `hash.txt` no existe o el hash ha expirado, se pedirá generar una nueva licencia.
- Este sistema es ideal para gestionar licencias temporales de software.

## Autor ✍️👨‍💻
Desarrollado por Daniel Zafra.

