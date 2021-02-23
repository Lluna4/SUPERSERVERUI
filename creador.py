import requests
import os 
import shutil

url = input("Cual es la url del server? ")
cambiado = True

print("descargando...")
archivo = requests.get(url, allow_redirects=True)
print("descarga completada")

with open("server2/server.jar", "wb") as jar:
    jar.write(archivo.content)




with open("server2\eula.txt", "w") as eula:
    eula.write("eula=true")
    cambiado == False


print("comprimiendo")
lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(lugar_del_archivo, "server2")

shutil.make_archive(archivo, 'zip', archivo)
#os.rename(archivo, "server1.15.1")