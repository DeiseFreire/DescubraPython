# 
# Arquivo com exemplos de loop
#

# Definindo um LOOP FOR
def loopFor():
    for x in range (5, 10):
        print (x)

loopFor()

# Usando um LOOP FOR em uma coleçao
def loopArray ():
    dias = ["seg", "ter", "quar", "quin", "sex", "sab", "dom"]
    for d in dias:
        print (d)

loopArray()

# Usando BREAK e CONTINUE

# Usando a função enumerate, para buscar valores e seus índices
def loopEnum ():
    dias = ["seg", "ter", "quar", "quin", "sex", "sab", "dom"]
    for i, d in enumerate(dias):
         print (i, d)
loopEnum()  
 
