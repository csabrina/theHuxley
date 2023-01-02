y= int(input())
count=0
media=0
qntIntervalo=0
for i in range(20):
  x= int(input())
  if x==-1:
    break
  if x==y:
    count +=1
  if 0<x<15 or 0<x>20:
    media +=x
    qntIntervalo+=1


 
print("O n�mero {} apareceu {} vez(es)" .format(y, count))
if qntIntervalo >0:
    print("A m�dia dos n�meros foi de: {:.2f}" .format(media/qntIntervalo))
else:
    print("Sem valores para calcular a m�dia")
  

