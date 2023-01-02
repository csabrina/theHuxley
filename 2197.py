qnt= int(input())
numeros=[]
letras=[]


for i in range(qnt):
  v1,v2=input().split()
  numeros.append(v1)
  letras.append(v2)


for x in range(qnt):
  pos= numeros.index(str(x+1))
  print("{}" .format(letras[pos]), end="")