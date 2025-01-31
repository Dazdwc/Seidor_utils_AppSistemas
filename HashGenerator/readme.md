# Generador de Hashes 🔑📅

## Descripción 📄🛠️

El Generador de Hashes es una herramienta diseñada para crear un hash de licencia con una validez definida en días. Este hash se usa para restringir el uso de una licencia dentro de un tiempo determinado, evitando el acceso no autorizado a un software.

Este proyecto consta de dos aplicaciones relacionadas:
1. **Generador de Hashes**: Permite generar un hash de licencia con una validez definida en días.
2. **License Manager**: Gestiona y verifica la validez de los hashes generados, asegurando que las claves sean legítimas y no hayan expirado.

Este sistema es útil para administrar licencias de software, restringiendo su uso a un periodo determinado y garantizando que los usuarios tengan acceso válido.

## Características ✨✅

- Verifica la validez del hash almacenado.
- Comprueba si la licencia ha expirado o sigue activa.
- Previene el acceso a software sin una licencia válida.

- Solicita al usuario la cantidad de días de validez.
- Genera un hash basado en una clave secreta y la fecha de expiración.
- Guarda el hash en un archivo de texto (`hash.txt`).

### Generador de Hashes:
- Solicita al usuario la cantidad de días de validez.
- Genera un hash basado en una clave secreta y la fecha de expiración.
- Guarda el hash en un archivo de texto (`hash.txt`).

### License Manager:
- Verifica la validez del hash almacenado.
- Comprueba si la licencia ha expirado o sigue activa.
- Previene el acceso a software sin una licencia válida.

## Requisitos ⚙️💻

- Python 3.x
- Librerías estándar de Python (`hashlib`, `time`, `os`)

## Instalación 📦🔧

No es necesario instalar librerías adicionales. Simplemente descarga los archivos y ejecútalos en un entorno de Python.

## Uso 🚀📌

### Verificar una licencia
Ejecuta el License Manager:
```sh
python license_manager.py
```
El programa verificará si el hash almacenado en `hash.txt` es válido o ha expirado.

### Generar un hash de licencia
Ejecuta el script del generador de hashes:
```sh
python generate_hash.py
```
Se solicitará la cantidad de días de validez y se generará un hash en `hash.txt`.

## Autor ✍️👨‍💻
Desarrollado por Daniel Zafra.