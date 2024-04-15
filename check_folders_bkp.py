from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import datetime

def check_folder_update(folder_id):
    # Credenciales del servicio (descargar desde la consola de Google Cloud)
    credentials = Credentials.from_service_account_file("./proyecto-notificar-bkps-39cbe3845c49.json", scopes=["https://www.googleapis.com/auth/drive"])

    # Crear el cliente de la API de Google Drive
    service = build("drive", "v3", credentials=credentials)

    # Obtener el nombre de la carpeta
    folder_response = service.files().get(fileId=folder_id, fields="name").execute()
    folder_name = folder_response.get("name", "Nombre de carpeta no encontrado")

    # Obtener la lista de archivos ordenados por fecha de modificación (el más reciente primero)
    response = service.files().list(q=f"'{folder_id}' in parents", spaces="drive", fields="files(id, name, modifiedTime)", orderBy="modifiedTime desc").execute()
    files = response.get("files", [])

    if not files:
        return False, "No se encontraron archivos en la carpeta especificada."

    # Obtener la fecha de modificación del archivo más reciente
    latest_file_modified_time = datetime.datetime.fromisoformat(files[0]['modifiedTime'][:-1])

    # Obtener la fecha actual
    current_date = datetime.datetime.now()

    # Comprobar si el archivo más reciente se modificó hoy
    if latest_file_modified_time.date() == current_date.date():
        return True, f"La sucursal '{folder_name}' subio el bkp correctamente. Última actualización: {latest_file_modified_time.strftime('%Y-%m-%d %H:%M:%S')}"
    else:
        return False, f"La sucursal '{folder_name}' no subio bkp correctamente hoy. Última actualización: {latest_file_modified_time.strftime('%Y-%m-%d %H:%M:%S')}"
