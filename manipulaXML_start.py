#
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.mindom

def manipulaXML():
    doc = xml.dom.mindom.parser("C:\\Users\\booth05-mgr2\\Desktop\\Exercícios - Descubra o Python\\Ch5\\exemploXML.xml")
    print("Nome da primeira tag:", str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName("firstname")
    print("O primeiro nome é: ", primeiroNome[0].firstChild.nodeValue) 
    for skill in doc.getElementsByTagName("skill"):
        print ("skill encontrado: ", skill.getAttribute("nome"))
        
manipulaXML()
