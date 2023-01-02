nacionalidade= input();
ocupacao= input();
qntArmas= int(input());
calibre= int(input());

if(qntArmas==0 and calibre==0):
  print("Liberado");

elif(nacionalidade=="E"):
  if(qntArmas==0):
    print("Liberado");
  if(qntArmas>0):
    print("Barrado");

elif(nacionalidade=="B"):
  if(ocupacao=="M"):
    print("Liberado");
  elif(ocupacao=="T" or ocupacao=="O"):
    if(qntArmas<=1 and calibre<=22):
      print("Liberado");
    else:
      print("Barrado");
  if(ocupacao=="C"):
    if(qntArmas<=2 and calibre<=38):
      print("Liberado");
    else:
      print("Barrado");
  

  