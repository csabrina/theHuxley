imovel= input();
diarias= int(input());
tv= int(input());
internet= int(input());

if(imovel=="STANDARD" and tv==0 and internet==0):
  print("{:.2f}" .format(diarias*150)); 

elif(imovel=="STANDARD" and tv!=0 and internet!=0):
  total= (diarias*150)+(tv*10)+(internet*15);
  print("{:.2f}" .format(total));

if(imovel=="PREMIUM" and tv==0 and internet==0):
  print("{:.2f}" .format(diarias*200)); 

elif(imovel=="PREMIUM" and tv!=0 and internet!=0):
  total= (diarias*200)+(tv*10)+(internet*15);
  print("{:.2f}" .format(total));


