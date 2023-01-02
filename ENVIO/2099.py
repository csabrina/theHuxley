ensinoMedio = input();
encceja = input();
nota = float(input());
escola = input();
renda = float(input());

if(ensinoMedio=="CLD" or ensinoMedio=="CVC" or ensinoMedio=="CSC" or ensinoMedio=="NCC"):
  
  if(ensinoMedio=="CVC" and escola=="PUB"):
    print("Voce terah direito a isencao");
  
  elif(ensinoMedio=="CLD"):
    if(escola=="PUB" or escola=="PCB"):
      if(renda<=1.431):
        print("Voce terah direito a isencao");
      else:
        print("Infelizmente voce nao tem direito a isencao");
    elif(escola=="PSB" or escola=="PPS" or escola=="PPB" or escola=="NFE"):
      print("Infelizmente voce nao tem direito a isencao")
  
  elif(ensinoMedio=="CSC" or ensinoMedio=="NCC"):
      print("Infelizmente voce nao tem direito a isencao");
 
  elif(ensinoMedio=="CLD"):
    if(encceja=="s"):
      if(400<=nota<800):
        print("Voce terah direito a isencao");
      elif(0<=nota<400):
        print("Infelizmente voce nao tem direito a isencao");
    elif(encceja=="n"):
      if(nota==-1):
        print("Infelizmente voce nao tem direito a isencao");
    elif(ensinoMedio=="CVC" or ensinoMedio=="CSC" or ensinoMedio=="NCC"):
      if(encceja=="s"):
        print("Infelizmente voce nao tem direito a isencao");
else:
  print("Informacao sobre ensino medio invalida")
  