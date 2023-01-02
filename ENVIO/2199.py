n= int(input());

expoente=1;
while True:
  if 3**expoente>n:
      expoente-=1;
      break
  expoente+=1;

fat=1;
while expoente>=1:
  fat*=expoente;
  expoente-=1;

print(fat);