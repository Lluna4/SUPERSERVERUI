from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import zipfile
import requests
import socket
import tqdm
from tqdm import tqdm
import tkinter
from tkinter import Tk
import shutil
import psutil

r = Tk()
r.withdraw()
r.clipboard_clear()
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
si = True
si2 = False
si3 = False
si4 = False

mem = psutil.virtual_memory()

gb = mem.total  / (1024.0 ** 3)

if gb < 3.0:
    si = input(f"No tienes suficiente ram para correr un servidor correctamente, seguir? tienes {gb} GB de ram")
    if si == "si":
        pass
    if si == "no":
        quit

print("Hola!, esto es una prueba para ver si lo drive funciona")
print("Vamos a empezar con unas simples preguntas,")
while si == True:
    
    i = input("la primera y mas importante: De que version queres el server? (De 1.16 a 1.12) o pon saltar si tienes ya un server ")
    if  i != "saltar":
        try: 
            i_int = int(i[:1])
            
        except ValueError:
            print("por favor ponga una version existente")
            
            si2 = True

        if si2 == False:
            
            if i != "saltar":
                try:
                    os.mkdir("server")
                except IOError:
                    shutil.rmtree("server", ignore_errors=True)
                    os.mkdir("server")
                
                try:
                    
                    archivo = requests.get(f"https://cdn.getbukkit.org/spigot/spigot-{i}.jar", allow_redirects=True, stream=True)
                    total_size_in_bytes= int(archivo.headers.get('content-length', 0))
                    if total_size_in_bytes < 2000000:

                        print("Ha ocurrido un error, quizas la version no existe o se ha escrito mal")
                    elif total_size_in_bytes > 2000000:
                        print("descargando")
                        block_size = 4096 #4 Kibibytes
                        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                        with open('server/server.jar', 'wb') as file:
                            for data in archivo.iter_content(block_size):
                                progress_bar.update(len(data))
                                file.write(data)
                        progress_bar.close()
  
                        print("se ha descargado")


                        with open("server/eula.txt", "w") as eula:
                            eula.write("eula=true")
                        si = False
                        si3 = True
                except requests.exceptions.RequestException:
                    print("Ha ocurrido un error, quizas la version no existe o se ha escrito mal")


    


    if i == "saltar":
        si = False
        si3 = True

while si3 == True:
    i2 = input("Que dificultad quieres? (de pacifico a hardcore) ")

    with open("server/server.properties", "w") as propedades:
        if i2 == "pacifico":
            dificultad = "peaceful"
            si3 = False
            si4 = True
        if i2 == "facil":
            dificultad = "easy"
            si3 = False
            si4 = True
        if i2 == "normal":
            dificultad = i2
            si3 = False
            si4 = True
        if i2 == "dificil":
            dificultad = "hard"
            si3 = False
            si4 = True
        if i2 == "hardcore":
            dificultad = "hard"
            propedades.write("hardcore=true")
            si3 = False
            si4 = True
        else:
            pass
with open("server/server.properties", "a") as propedades:
    propedades.write(f"\ndifficulty={dificultad}")
while si4 == True:
    i3 = input("Que modo? (survival, creativo o aventura) ")
    with open("server/server.properties", "a") as propedades:
        if i3 == "survival":
            propedades.write("\ngamemode=0")
            si4 = False
        if i3 == "creativo":
            propedades.write("\ngamemode=1")
            si4 = False
        if i3 == "aventura":
            propedades.write("\ngamemode=2")
            si4 = False
        else:
            pass

ip = socket.gethostbyname(socket.gethostname())
with open("server/server.properties", "a") as propedades:
    propedades.write(f"\nip={ip}")
ip_str = str(ip)
r.clipboard_append(ip_str)
r.update()


i4 = input("Quieres que el mundo se suba automaticamente a drive y se descargue cuando se abra el servidor? si dices que si, se te preguntara la cuenta de google ")

if i4 == "si":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("server/DBCRD.txt")
    drive = GoogleDrive(gauth)
    world = drive.CreateFile({'title': 'world.txt'})
    world.Upload()
    overworld = drive.ListFile().GetList()
    print("creando los archivos de drive...")
    for file in overworld:
        id1 = file["id"]
        
    world_nether = drive.CreateFile({'title': 'world_nether.txt'})
    world_nether.Upload()
    nether = drive.ListFile().GetList()
    for file in nether:
        id2 = file["id"]
    world_the_end = drive.CreateFile({'title': 'world_the_end.txt'})
    world_the_end.Upload()
    end = drive.ListFile().GetList()
    for file in end:
        id3 = file["id"]


    with open("server/world_id.txt", "w") as world_id:
        world_id.write(id1)
    
    with open("server/world_nether_id.txt", "w") as world_nether_id:
        world_nether_id.write(id2)
    
    with open("server/world_the_end_id.txt", "w") as world_the_end_id:
        world_the_end_id.write(id3)
    
    print("creados!")
    
    with open("server/start.bat", "w") as start:
        start.write("python descargar_drive.py")
        start.write("\njava -Xms1G -Xmx3G -jar server.jar -nogui") #-nogui funciona a veces
        start.write("\npython drive_flojito.py")
        start.write("\nPAUSE")
    print("descargando scripts!")
    descargar = drive.CreateFile({'id': "1F1GuxKgRtyk7ziVmVvdR9JN0ZEcWBGlw"})
    descargar.GetContentFile("server/descargar_drive.py")
    subir = drive.CreateFile({'id': "1_Awy6gc7HVTIRyCdRUveLrPv5puJbhAv"})
    subir.GetContentFile("server/drive_flojito.py")
    secreto = drive.CreateFile({'id': "1f1tFSG3ZZLBGgb032kDbOAS0Fzj3KMIc"})
    secreto.GetContentFile("server/client_secrets.json")
    print("hecho!")
    
else:
    with open("server/start.bat", "w") as start:

        start.write("\njava -Xms1G -Xmx3G -jar server.jar -nogui") #-nogui funciona a veces

        start.write("\nPAUSE")
    
    print(f"Tu ip es: {ip}, se te ha copiado en el portapapeles")

    

    



  

        

