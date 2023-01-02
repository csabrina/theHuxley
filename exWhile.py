'''
contador = 0

while(contador < 9):
  print("O valor do contador é %d" %contador)
  contador +=1

print("Loop encerrado!")

#While com variavel de controle

controle=""
while(controle!="s"):
  print("a. Pagar")
  print("b. Receber")
  print("c. Consultar")
  print("s. Sair")
  controle=input("Digite a opção desejada:")

print("Loop encerrado!")
'''
var= 20

while(var>0):
  print("O valor de var é %d" %var) #enquanto var for maior que 0, escreva o valor de var
  var -= 1
  if(var==11):
    break

print("Loop interrompido no valor 11")