import os
import psutil
import logging
from pathlib import Path

# Configurar el sistema de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir extensiones de archivos sospechosos
EXTENSIONES_SOSPECHOSAS = {'.exe', '.vbs', '.bat', '.js'}

# Definir nombres de procesos maliciosos conocidos
PROCESOS_MALICIOSOS = {'badprocess.exe', 'malware.exe'}

# Función para eliminar archivos sospechosos
def eliminar_archivos_sospechosos(directorio_base="C:\\"):
    directorio_base = Path(directorio_base)
    if not directorio_base.exists() or not directorio_base.is_dir():
        logging.warning(f"Directorio no válido: {directorio_base}")
        return
    
    for ruta_actual, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            if Path(archivo).suffix in EXTENSIONES_SOSPECHOSAS:
                ruta_completa = Path(ruta_actual) / archivo
                try:
                    os.remove(ruta_completa)
                    logging.info(f"Eliminado: {ruta_completa}")
                except PermissionError:
                    logging.warning(f"Permiso denegado al intentar eliminar: {ruta_completa}")
                except Exception as e:
                    logging.error(f"Error al eliminar {ruta_completa}: {e}")

# Función para terminar procesos maliciosos
def eliminar_procesos_maliciosos():
    for proceso in psutil.process_iter(attrs=['pid', 'name']):
        try:
            nombre_proceso = proceso.info['name'].lower()
            if nombre_proceso in PROCESOS_MALICIOSOS:
                psutil.Process(proceso.info['pid']).terminate()
                logging.info(f"Proceso eliminado: {nombre_proceso} (PID: {proceso.info['pid']})")
        except psutil.NoSuchProcess:
            logging.warning(f"El proceso {nombre_proceso} ya no existe.")
        except psutil.AccessDenied:
            logging.error(f"No se tienen permisos para eliminar el proceso {nombre_proceso}.")
        except Exception as e:
            logging.error(f"Error al intentar eliminar {nombre_proceso}: {e}")

# Función principal de mitigación de amenazas
def main():
    logging.info("Iniciando proceso de mitigación de malware...")
    eliminar_archivos_sospechosos()
    eliminar_procesos_maliciosos()
    logging.info("Proceso de mitigación de malware completado.")

if __name__ == "__main__":
    main()
