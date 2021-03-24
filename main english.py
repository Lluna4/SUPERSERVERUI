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

print(f"tienes {gb} GB de ram")

if gb < 3.0:
    si = input(f"You don't have enough ram for hosting a server continue? You have {gb} GB of ram")
    if si == "yes":
        pass
    if si == "no":
        quit

#print("Hola!, esto es una prueba para ver si lo drive funciona")
print("We will be beginning with simple questions,")

while si == True:
    
    i = input("The first and the most important: Which version do you want for the server? write skip if you have already one server")
    if  i != "skip":
        try: 
            i_int = int(i[:1])
            
        except ValueError:
            print("please write an existing version")
            
            si2 = True

        if si2 == False:
            
            if i != "skip":
                try:
                    os.mkdir("server")
                except IOError:
                    shutil.rmtree("server", ignore_errors=True)
                    os.mkdir("server")
                
                try:
                    
                    archivo = requests.get(f"https://cdn.getbukkit.org/spigot/spigot-{i}.jar", allow_redirects=True, stream=True)
                    total_size_in_bytes= int(archivo.headers.get('content-length', 0))
                    if total_size_in_bytes < 2000000:

                        print("Error, maybe you wrote something wrong in the verion")
                    elif total_size_in_bytes > 2000000:
                        print("descargando")
                        block_size = 4096 #4 Kibibytes
                        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                        with open('server/server.jar', 'wb') as file:
                            for data in archivo.iter_content(block_size):
                                progress_bar.update(len(data))
                                file.write(data)
                        progress_bar.close()
  
                        print("Downloaded!")


                        with open("server/eula.txt", "w") as eula:
                            eula.write("eula=true")
                        si = False
                        si3 = True
                except requests.exceptions.RequestException:
                    print("Error, maybe you wrote something wrong in the verion")


    


    if i == "skip":
        si = False
        si3 = True

while si3 == True:
    i2 = input("What difficulty you want? (from peaceful to hardcore) ")

    with open("server/server.properties", "w") as propedades:
        if i2 == "peaceful":
            dificultad = "peaceful"
            si3 = False
            si4 = True
        if i2 == "easy":
            dificultad = "easy"
            si3 = False
            si4 = True
        if i2 == "normal":
            dificultad = i2
            si3 = False
            si4 = True
        if i2 == "hard":
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
    i3 = input("Which mode do you want (survival, creative or adventure) ")
    with open("server/server.properties", "a") as propedades:
        if i3 == "survival":
            propedades.write("\ngamemode=0")
            si4 = False
        if i3 == "creative":
            propedades.write("\ngamemode=1")
            si4 = False
        if i3 == "adventure":
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


i4 = input("Do you want the world to be uploaded to google drive? ")

if i4 == "yes":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("server/DBCRD.txt")
    drive = GoogleDrive(gauth)
    world = drive.CreateFile({'title': 'world.txt'})
    world.Upload()
    overworld = drive.ListFile().GetList()
    print("Creating files...")
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
    
    print("created!")
    if gb < 8.0:
        with open("server/start.bat", "w") as start:
            start.write("python descargar_drive.py")
            start.write("\njava -Xms1G -Xmx3G -jar server.jar -nogui") #-nogui funciona a veces
            start.write("\npython drive_flojito.py")
            start.write("\nPAUSE")
    if gb < 16.0 and gb > 8.0:
        with open("server/start.bat", "w") as start:
            start.write("python descargar_drive.py")
            start.write("\njava -Xms1G -Xmx6G -jar server.jar -nogui") #-nogui funciona a veces
            start.write("\npython drive_flojito.py")
            start.write("\nPAUSE")      

    print("downloading scripts!")
    descargar = drive.CreateFile({'id': "1F1GuxKgRtyk7ziVmVvdR9JN0ZEcWBGlw"})
    descargar.GetContentFile("server/descargar_drive.py")
    subir = drive.CreateFile({'id': "1_Awy6gc7HVTIRyCdRUveLrPv5puJbhAv"})
    subir.GetContentFile("server/drive_flojito.py")
    secreto = drive.CreateFile({'id': "1f1tFSG3ZZLBGgb032kDbOAS0Fzj3KMIc"})
    secreto.GetContentFile("server/client_secrets.json")
    print("done!")
    
else:
    if gb < 8.0:

        with open("server/start.bat", "w") as start:

            start.write("\njava -Xms1G -Xmx3G -jar server.jar -nogui") #-nogui funciona a veces

            start.write("\nPAUSE")
    
    if gb < 16.0 and gb > 8.0:

        with open("server/start.bat", "w") as start:

            start.write("\njava -Xms1G -Xmx6G -jar server.jar -nogui") #-nogui funciona a veces

            start.write("\nPAUSE")
    
print(f"Your ip is: {ip}, it has been copied in the clipboard")

    

    



  

        

