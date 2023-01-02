idade= int(input());
jogo= input();

if(idade>=1 and idade<=130):
    if(jogo=="azar" or jogo=="mmorpg" or jogo=="moba" or jogo=="casual"):
      
      if(jogo=="azar"):
        if(idade>=21):
          print("Pode entrar!");
        else:
          print("Volte daqui há alguns anos.");

      elif(jogo=="mmorpg"):
        if(idade>=14):
          print("Pode entrar!");
        else:
          print("Volte daqui há alguns anos.");
        
      elif(jogo=="moba"):
        if(idade>=10): 
          print("Pode entrar!");
        else:
          print("Volte daqui há alguns anos.");
        
      elif(jogo=="casual"):
        print("Pode entrar!");   

    else:
      print("Jogo invalido.");
else:
  print("Idade invalida.");