#
# Arquivo com exemplos 
#

# definindo uma função básica

def func1():
    print ("Eu sou uma função")
func1()

# a função que recebe argumentos

def func2 (arg1, arg2):
    print (arg1 + " " + arg2)
func2 ("Deise", "Freire")

# função que retorna um valor

def cubo (x):
    return x* x* x

f = cubo (3)
print (f)
print (cubo(2))


