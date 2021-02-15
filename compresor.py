import shutil
import os

lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(lugar_del_archivo, "server")

shutil.make_archive(archivo, 'zip', archivo)