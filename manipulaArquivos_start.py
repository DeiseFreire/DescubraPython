#
# Exemplos de como trabalhar com arquivos
# 

import os 
from os import path
import shutil

def copiarArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.realpath("NovoArquivo.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        shutil.copystat(pathAtual, novoPath)

#copiarArquivo()

def renomearArquivo():
    if path.exists("NovoArquivo.txt.bkp"):
       os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")
renomearArquivo()     

