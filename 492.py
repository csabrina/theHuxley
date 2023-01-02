capsulas=0;

for i in range(7):  
  quantidade= int(input());
  tamanho= input().upper();

  if(tamanho=="P"):
    capsulas+=quantidade*10;
  else:
    capsulas+= quantidade*16;

print(capsulas)
print(int(capsulas*2/7));

