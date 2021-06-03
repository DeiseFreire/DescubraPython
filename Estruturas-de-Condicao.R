#
# Fonte da ideia: 
# FGV / IBRE – Estatística com R: 05 Estruturas de Condição. Produção Fundação Getúlio Vargas. [S. l.]: FGV, 2014. 1 videoaula (7min.26seg.).
#

# Exemplo 1: Considere o triângullo abaixo, informe se ele é escaleno.

# Lados do triângulo

a <- 1
b <- 2
c <- 3

# Estrutura de condição 

if (a != b & b != c & c != a){
  cat ("É um triângulo escaleno.")
}

# Exemplo 2: Crie dois objetos a e b numéricos e diferentes e informe o maior deles.
# Dois objetos numéricos 
a <- 2 
b <- 5
# Estrutura de condição
if (a > b) {
  cat (a)
} else {
  cat (b)
}
# EXEMPLO 3: Calcule a raiz quadrada de um número se for positivo. Caso seja negativo, retorne a seguinte mensagem: "O número é negativo".
X <- -25
ifelse (x >= 0, sqrt(x), "O número é negativo" )
# Exercício 
# Informe se um número é par ou ímpar usando a estrutura de condição ifelse.
