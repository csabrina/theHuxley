bairro= input();

if(bairro=="Flash" or bairro=="Arrow" or bairro=="Legends of Tomorrow" or bairro=="Super Girl"):
  dia= input();
  if(dia=="ter�a"):
    horario= int(input());
    if(8<=horario<=20):
      print("chegou �gua");
    else:
      print("n�o chegou �gua");
    
elif(bairro=="Agent Carter" or bairro=="Demolidor" or bairro=="Agentes da Shield"):
  dia= input();
  if(dia=="quarta"):
    horario= int(input());
    if(24>=horario>=2):
      print("chegou �gua");
    else:
      print("n�o chegou �gua");
    
else:
  print("Bairro Inv�lido");
  