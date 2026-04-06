"""
================================================
app.py — Script de mitigación de malware
================================================
Proyecto : NovaBank (Simulación educativa de phishing)
Curso    : CLV-0062 | Universidad Fidélitas
Autor    : orami13

Propósito:
    Este script demuestra la FASE DE MITIGACIÓN del ciclo de un ataque.
    Simula cómo un software antimalware básico detecta y elimina
    archivos y procesos sospechosos en un sistema Windows.

ADVERTENCIA:
    - Ejecutar solo en entorno controlado (máquina virtual o sandbox).
    - Requiere privilegios de administrador.
    - Diseñado para Windows. En Linux/macOS se deben modificar las rutas.
    - NO usar en sistemas reales sin comprender completamente el código.
================================================
"""

# ------------------------------------------------
# IMPORTACIÓN DE MÓDULOS
# Los módulos son bibliotecas de código ya escrito que podemos reutilizar.
# Se importan al inicio del script, antes de cualquier otra instrucción.
# ------------------------------------------------

import os

# os: módulo estándar de Python para interactuar con el sistema operativo.
# Permite leer directorios, eliminar archivos, obtener rutas, etc.

import psutil

# psutil: módulo de terceros (se instala con pip) para monitorear
# procesos del sistema operativo y recursos del hardware (CPU, RAM, disco).
# Requiere instalación: pip install psutil

import logging

# logging: módulo estándar de Python para registrar mensajes del programa.
# Es mejor práctica que usar print() porque permite niveles de severidad
# y guardar los registros en archivos de log.

from pathlib import Path

# pathlib: módulo estándar para trabajar con rutas de archivos y carpetas
# de forma orientada a objetos. Es más moderno y legible que os.path.
# "from pathlib import Path" importa solo la clase Path, no todo el módulo.


# ------------------------------------------------
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# Configura cómo se verán y comportarán los mensajes de registro.
# ------------------------------------------------

logging.basicConfig(
    # basicConfig() = configura el sistema de logging con opciones básicas
    level=logging.INFO,
    # level = nivel mínimo de mensajes a registrar.
    # Niveles disponibles (de menor a mayor severidad):
    # DEBUG < INFO < WARNING < ERROR < CRITICAL
    # Con INFO, se registran mensajes de INFO, WARNING, ERROR y CRITICAL,
    # pero NO los de DEBUG.
    format="%(asctime)s - %(levelname)s - %(message)s",
    # format = plantilla para el formato de cada línea del log.
    # %(asctime)s   = fecha y hora del mensaje (ej: 2024-03-15 10:30:45,123)
    # %(levelname)s = nivel del mensaje (ej: INFO, WARNING, ERROR)
    # %(message)s   = el texto del mensaje en sí
)


# ------------------------------------------------
# CONSTANTES DEL PROGRAMA
# Las constantes son variables cuyo valor no cambia durante la ejecución.
# Por convención en Python, se escriben en MAYÚSCULAS_CON_GUIONES.
# ------------------------------------------------

EXTENSIONES_SOSPECHOSAS = {".exe", ".vbs", ".bat", ".js"}
# Set (conjunto) de extensiones de archivo consideradas sospechosas.
# Se usa un set {} en lugar de una lista [] porque:
# 1. No permite duplicados
# 2. La búsqueda (operador "in") es más rápida en sets que en listas
# Estas extensiones son comunes en malware real:
# .exe = ejecutables de Windows
# .vbs = Visual Basic Script (frecuentemente usado en malware)
# .bat = archivos de comandos de Windows (batch)
# .js  = JavaScript (puede ejecutarse en Windows con wscript.exe)

PROCESOS_MALICIOSOS = {"badprocess.exe", "malware.exe"}
# Set de nombres de procesos considerados maliciosos.
# En este proyecto educativo, son nombres ficticios.
# En un antimalware real, esta lista sería mucho más extensa
# y se actualizaría constantemente desde una base de datos.

DIRECTORIO_ESCANEO = "C:\\"
# Directorio raíz donde comenzará el escaneo de archivos.
# "C:\\" = raíz del disco C en Windows.
# La doble barra invertida \\ es necesaria en Python porque \ es un
# carácter de escape. \\ representa una sola barra invertida real.


# ------------------------------------------------
# FUNCIÓN: ELIMINAR ARCHIVOS SOSPECHOSOS
# Recorre un directorio y sus subdirectorios buscando
# archivos con extensiones de la lista EXTENSIONES_SOSPECHOSAS.
# ------------------------------------------------


def eliminar_archivos_sospechosos(directorio_base=DIRECTORIO_ESCANEO):
    """
    Escanea un directorio recursivamente y elimina archivos con extensiones sospechosas.

    Args:
        directorio_base (str): Ruta del directorio donde comenzar el escaneo.
                               Por defecto usa la constante DIRECTORIO_ESCANEO.
    """
    # def = palabra clave para definir una función
    # directorio_base=DIRECTORIO_ESCANEO = parámetro con valor por defecto
    # Si no se pasa ningún argumento al llamar la función, usará DIRECTORIO_ESCANEO

    directorio_base = Path(directorio_base)
    # Convierte la cadena de texto a un objeto Path.
    # Path("C:\\") crea un objeto que representa la ruta de forma orientada a objetos,
    # lo que facilita operaciones como verificar si existe, unir rutas, obtener extensión, etc.

    if not directorio_base.exists() or not directorio_base.is_dir():
        # .exists() = verifica si la ruta existe en el sistema de archivos
        # .is_dir() = verifica si la ruta es un directorio (no un archivo)
        # not = operador lógico de negación
        # or = operador lógico: la condición es verdadera si CUALQUIERA de las dos es verdadera
        logging.warning(f"Directorio no válido: {directorio_base}")
        # logging.warning() = registra un mensaje de nivel WARNING
        # f"..." = f-string: permite insertar variables dentro de una cadena con {variable}
        return
        # return sin valor = termina la función inmediatamente y no devuelve nada

    logging.info(f"Iniciando escaneo en: {directorio_base}")
    # logging.info() = registra un mensaje informativo (nivel INFO)

    for ruta_actual, subcarpetas, archivos in os.walk(directorio_base):
        # os.walk() = generador que recorre un directorio y TODOS sus subdirectorios.
        # En cada iteración devuelve una tupla con 3 valores:
        # ruta_actual = ruta de la carpeta que se está revisando en este momento (str)
        # subcarpetas = lista de nombres de subdirectorios dentro de ruta_actual (no los usamos)
        # archivos    = lista de nombres de archivos dentro de ruta_actual

        for archivo in archivos:
            # Recorre cada archivo encontrado en la carpeta actual

            extension = Path(archivo).suffix
            # Path(archivo).suffix = obtiene la extensión del archivo
            # Ejemplo: Path("malware.exe").suffix devuelve ".exe"

            if extension in EXTENSIONES_SOSPECHOSAS:
                # in = operador que verifica si un valor está dentro de un conjunto/lista
                # Si la extensión está en nuestro set de extensiones sospechosas...

                ruta_completa = Path(ruta_actual) / archivo
                # Path(ruta_actual) / archivo = construye la ruta completa del archivo
                # El operador / en objetos Path une rutas de forma segura
                # Ejemplo: Path("C:\\Users") / "malware.exe" = Path("C:\\Users\\malware.exe")

                try:
                    # try = bloque que intenta ejecutar código que podría causar un error.
                    # Si ocurre un error, se captura en los bloques except correspondientes.

                    os.remove(ruta_completa)
                    # os.remove() = elimina el archivo en la ruta indicada.
                    # Si el archivo no existe o no hay permisos, lanza una excepción.

                    logging.info(f"Archivo eliminado: {ruta_completa}")
                    # Registra que el archivo fue eliminado exitosamente

                except PermissionError:
                    # PermissionError = excepción que se lanza cuando no hay permisos
                    # para realizar una operación (leer, escribir, eliminar, etc.)
                    logging.warning(f"Permiso denegado: {ruta_completa}")

                except FileNotFoundError:
                    # FileNotFoundError = excepción cuando el archivo no existe.
                    # Puede ocurrir si otro proceso eliminó el archivo entre el escaneo y la eliminación.
                    logging.warning(f"Archivo no encontrado: {ruta_completa}")

                except Exception as e:
                    # Exception = clase base de todas las excepciones en Python.
                    # "as e" = guarda la excepción en la variable "e" para poder mostrar el mensaje.
                    # Este bloque captura cualquier otro error no previsto.
                    logging.error(f"Error al eliminar {ruta_completa}: {e}")
                    # logging.error() = registra un mensaje de nivel ERROR (más severo que WARNING)


# ------------------------------------------------
# FUNCIÓN: TERMINAR PROCESOS MALICIOSOS
# Revisa todos los procesos activos en el sistema y termina
# aquellos cuyos nombres están en PROCESOS_MALICIOSOS.
# ------------------------------------------------


def eliminar_procesos_maliciosos():
    """
    Recorre los procesos activos del sistema y termina aquellos
    cuyos nombres coinciden con la lista PROCESOS_MALICIOSOS.
    """

    logging.info("Escaneando procesos activos...")

    for proceso in psutil.process_iter(attrs=["pid", "name"]):
        # psutil.process_iter() = generador que itera sobre todos los procesos activos.
        # attrs=["pid", "name"] = especifica qué atributos queremos obtener de cada proceso:
        # pid  = Process ID: número único que identifica cada proceso en el sistema
        # name = nombre del ejecutable del proceso (ej: "chrome.exe", "python.exe")

        try:
            nombre_proceso = proceso.info["name"].lower()
            # proceso.info = diccionario con los atributos solicitados en attrs
            # ["name"] = accede al nombre del proceso
            # .lower() = convierte el nombre a minúsculas para comparación sin distinción
            # Ejemplo: "Malware.EXE" → "malware.exe"

            if nombre_proceso in PROCESOS_MALICIOSOS:
                # Verifica si el nombre del proceso está en nuestra lista de procesos maliciosos

                pid = proceso.info["pid"]
                # Obtiene el PID (identificador numérico) del proceso

                psutil.Process(pid).terminate()
                # psutil.Process(pid) = crea un objeto que representa el proceso con ese PID
                # .terminate() = envía una señal de terminación al proceso.
                # En Windows envía SIGTERM; en Unix es más suave que .kill()

                logging.info(f"Proceso terminado: {nombre_proceso} (PID: {pid})")

        except psutil.NoSuchProcess:
            # psutil.NoSuchProcess = excepción cuando el proceso ya no existe.
            # Puede ocurrir si el proceso terminó entre el momento en que lo encontramos
            # y el momento en que intentamos acceder a él.
            logging.warning(f"El proceso ya no existe (puede haber terminado solo).")

        except psutil.AccessDenied:
            # psutil.AccessDenied = excepción cuando no hay permisos suficientes
            # para acceder o terminar el proceso (requiere privilegios de administrador).
            logging.error(
                f"Acceso denegado para terminar: {nombre_proceso}. Se requieren privilegios de administrador."
            )

        except Exception as e:
            # Captura cualquier otro error inesperado
            logging.error(f"Error inesperado con proceso: {e}")


# ------------------------------------------------
# FUNCIÓN PRINCIPAL
# Es el punto de entrada del programa: coordina y llama
# a todas las demás funciones en el orden correcto.
# ------------------------------------------------


def main():
    """
    Función principal. Coordina el proceso completo de mitigación:
    1. Elimina archivos con extensiones sospechosas
    2. Termina procesos maliciosos conocidos
    """

    logging.info("=" * 50)
    # "=" * 50 = repite el carácter "=" 50 veces (separador visual en el log)

    logging.info("NovaBank — Script de mitigación de malware")
    logging.info("PROYECTO EDUCATIVO | CLV-0062 | Universidad Fidélitas")
    logging.info("=" * 50)
    logging.info("Iniciando proceso de mitigación...")

    eliminar_archivos_sospechosos()
    # Llama a la función de escaneo y eliminación de archivos

    eliminar_procesos_maliciosos()
    # Llama a la función de detección y terminación de procesos

    logging.info("=" * 50)
    logging.info("Proceso de mitigación completado.")
    logging.info("=" * 50)


# ------------------------------------------------
# PUNTO DE ENTRADA DEL SCRIPT
# Esta condición verifica si el script se está ejecutando directamente
# (no siendo importado como módulo por otro script).
# ------------------------------------------------

if __name__ == "__main__":
    # __name__ = variable especial de Python.
    # Cuando el script se ejecuta directamente (python app.py), __name__ vale "__main__".
    # Cuando el script es importado por otro archivo, __name__ vale el nombre del módulo.
    # Esta estructura permite que el código en main() solo corra cuando
    # ejecutamos este archivo directamente.

    main()
    # Llama a la función principal para iniciar el programa
