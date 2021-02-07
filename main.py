from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
gauth.LoadCredentialsFile("DBCRD.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("DBCRD.txt")
drive = GoogleDrive(gauth)

try:
    os.mkdir("server")
except IOError:
    pass

print("Hola!, esto es una prueba para ver si lo drive funciona")

i = input("Vamos a empezar con unas simples preguntas, la primera y mas importante: De que version queres el server? (De 1.16 a 1.12)")

if i == "1.16.4":
    print("Comienza la descarga del servidor...")
    server = drive.CreateFile({'id': "1EiZGKJ8H5Wzqd7MWotzwapPV-9nhxbyW"})
    lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
    archivo2 = os.path.join(lugar_del_archivo, "server/server.zip")
    server.GetContentFile(archivo2)
    print("se ha acabado la descarga del servidor")