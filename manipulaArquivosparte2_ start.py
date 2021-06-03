#
# Exemplos de como trabalhar com arquivos
#

import os 
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def CriaZipModo1():
        shutil1.make_archive("ArquivoCompactado", "zip", "C:\\Users\\booth05-mgr2\\Desktop\\Exercícios - Descubra o Python\\Ch3")

#CriaZipModo1()

def CriaZipModo2():
        with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
            novoZip.write("NovoArquivo.bkp")
            novoZip.write("NovoArquivo.txt")
            novoZip.write("NovoArquivo.zip")

#CriaZipModo2()

def DeleteArquivo():
    os.remove("ArquivoZipModo2.zip")

DeleteArquivo()