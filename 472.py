nome= input().upper();
assinatura= int(input());

if(nome=="MURAL"):
  total= 200.00*assinatura;
  print("{:.2f}" .format(total));

elif(nome=="O CORETO"):
  total= 235.00*assinatura;
  print("{:.2f}" .format(total));

elif(nome=="MEU LAR"):
  total= (180.00*assinatura)*0.9;
  print("{:.2f}" .format(total));

elif(nome=="SUA MESA"):
  total= (230.00*assinatura)*0.9;
  print("{:.2f}" .format(total));
  