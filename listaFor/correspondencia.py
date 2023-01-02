soma=0;
contador=0;

for x in range (7):
  cartas=int(input());
  soma+= cartas;
  if cartas >=100:
    contador= contador+1;

print(contador)
print("{:.0f}" .format(soma/7));