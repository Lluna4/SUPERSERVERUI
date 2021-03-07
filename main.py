from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import zipfile
import requests
import socket

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



print("Hola!, esto es una prueba para ver si lo drive funciona")

i = input("Vamos a empezar con unas simples preguntas, la primera y mas importante: De que version queres el server? (De 1.16 a 1.12) o pon saltar si tienes ya un server ")
os.mkdir("server")
if i == "1.16.5":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")
if i == "1.16.4":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.4.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "1.16.3":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.3.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "1.16.2":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.2.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "1.16.1":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.16.1.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")


if i == "1.15.2":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "1.15.1":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.15.1.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "1.15":
    print("descargando")
    archivo = requests.get("https://cdn.getbukkit.org/spigot/spigot-1.15.jar", allow_redirects=True)
    print("se ha descargado")
    with open("server/server.jar", "wb") as jar:
        jar.write(archivo.content)
    with open("server/eula.txt", "x") as eula:
        eula.write("eula=true")

if i == "saltar":
    pass
# se contiua con las diferentes versiones

i2 = input("Que dificultad quieres? (de pacifico a hardcore) ")

with open("server/server.properties", "x") as propedades:
    if i2 == "pacifico":
        dificultad = "peaceful"
    if i2 == "facil":
        dificultad = "easy"
    if i2 == "normal":
        dificultad = i2
    if i2 == "dificil":
        dificultad = "hard"
    if i2 == "hardcore":
        dificultad = "hard"
        propedades.write("hardcore=true")
    propedades.write(f"\ndifficulty={dificultad}")

    i3 = input("Que modo? (survival, creativo o aventura) ")

    if i3 == "survival":
        propedades.write("\ngamemode=0")
    if i3 == "creativo":
        propedades.write("\ngamemode=1")
    if i3 == "aventura":
        propedades.write("\ngamemode=2")
    ip = socket.gethostbyname(socket.gethostname())

    propedades.write(f"\nip={ip}")


i4 = input("Quieres que el mundo se suba automaticamente a drive y se descargue cuando se abra el servidor? si dices que si, se te preguntara la cuenta de google ")

if i4 == "si":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("DBCRD.txt")
    drive = GoogleDrive(gauth)
    world = drive.CreateFile({'title': 'world.txt'})
    world.Upload()
    world_nether = drive.CreateFile({'title': 'world_nether.txt'})
    world_nether.Upload()
    world_the_end = drive.CreateFile({'title': 'world_the_end.txt'})
    world_the_end.Upload()
    id1 = world.GetPermissions()
    id1 = str(id1[0])
    id1 = id1[77:-371]

    id2 = world_nether.GetPermissions()
    id2 = str(id2[0])
    id2 = id2[77:-371]

    id3 = world_the_end.GetPermissions()
    id3 = str(id3[0])
    id3 = id3[77:-371]

    with open("world_id.txt", "w") as world_id:
        world_id.write(id1)
    
    with open("world_nether_id.txt", "w") as world_nether_id:
        world_nether_id.write(id2)
    
    with open("world_the_end_id.txt", "w") as world_the_end_id:
        world_the_end_id.write(id3)
    
    with open("server/start.bat", "w") as start:
        start.write("python descargar_drive.py")
        start.write("\njava -Xms1G -Xmx3G -jar server.jar -nogui")
        start.write("\npython drive_flojito.py")
        start.write("\nPAUSE")
    
    #A partir de aqui se descargan drive_flojito y descargar_drive (cuando esten acabados)

        

