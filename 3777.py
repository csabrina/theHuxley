dia= int(input());
estudante= int(input());
socio= int(input());

if(estudante==0 and socio==0):
  if( dia==1 or dia==2 or dia==3 or dia==4):
    total= 15;
    print("COMUM: R$ {:.2f}" .format(total));
  elif(dia==5 or dia==6 or dia==7):
    total= 15*2;
    print("COMUM: R$ {:.2f}" .format(total));
    
elif(estudante==1 and socio==0):
  if(dia==1 or dia==2 or dia==3 or dia==4):
    total=15*0.7;
    print("ESTUDANTE: R$ {:.2f}" .format(total));
  elif(dia==5 or dia==6 or dia==7):
    total=(15*2)*0.7;
    print("ESTUDANTE: R$ {:.2f}" .format(total));
    
elif(estudante==0 and socio==1):
  if(dia==1 or dia==2 or dia==3 or dia==4):
    total=15;
    print("SOCIO: R$ {:.2f}" .format(total));
  elif(dia==5 or dia==6 or dia==7):
    total=(15*2)*0.8;
    print("SOCIO: R$ {:.2f}" .format(total));
    
else:
  print("Um cliente não pode ser sócio e estudante");
  
  