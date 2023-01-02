v= input();

if (v=="Homem de Ferro" or v=="Thor" or v=="Capitão América" or v=="Thor" or v=="Gavião Arqueiro" or v=="Viúva Negra"):
  poder= input(); 
  energia= int(input());

  if v=="Homem de Ferro":
    if poder=="Armadura de Ferro": 
      if energia>=10:
        print("Homem de Ferro conseguiu derrotar Thanos");
      elif energia<10:
        print("Homem de Ferro NAO conseguiu derrotar Thanos, chamem outro Vingador");
    
    elif poder== "Força Bruta":
        print("Homem de Ferro NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Hulk");
      
    elif poder== "Escudo":
        print("Homem de Ferro NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Capitão América");
      
    elif poder== "Martelo":
        print("Homem de Ferro NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Thor");
      
    elif poder== " Arco e Flecha":
        print("Homem de Ferro NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Gavião Arqueiro");
      
    elif poder=="Inteligência":
        print("Homem de Ferro NAO conseguiu derrotar Thanos");
        print("Esse é o poder da Viúva Negra");
    
  elif v=="Hulk":
    if poder=="Força Bruta":
      if energia>=5:
        print("Hulk conseguiu derrotar Thanos");
      elif energia<5:
        print("Hulk NAO conseguiu derrotar Thanos, chamem outro Vingador");
            
    elif poder=="Armadura de Ferro":
      print("Hulk NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Homem de Ferro");
      
    elif poder== "Escudo":
      print("Hulk NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Capitão América");
      
    elif poder== "Martelo":
      print("Hulk NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Thor");
      
    elif poder== "Arco e Flecha":
      print("Hulk NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Gavião Arqueiro");
      
    elif poder=="Inteligência":
      print("Hulk NAO conseguiu derrotar Thanos");
      print("Esse é o poder da Viúva Negra");

  elif v=="Capitão América":
    if poder=="Escudo": 
      if energia>=7:
        print("Capitão América conseguiu derrotar Thanos");
      elif energia<7:
        print("Capitão América NAO conseguiu derrotar Thanos, chamem outro Vingador");
    
    elif poder== "Força Bruta":
        print("Capitão América NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Hulk");
      
    elif poder== "Armadura de Ferro":
        print("Capitão América NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Homem de Ferro");
      
    elif poder== "Martelo":
        print("Capitão América NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Thor");
      
    elif poder== "Arco e Flecha":
        print("Capitão América NAO conseguiu derrotar Thanos");
        print("Esse é o poder do Gavião Arqueiro");
      
    elif poder=="Inteligência":
        print("Capitão América NAO conseguiu derrotar Thanos");
        print("Esse é o poder da Viúva Negra");
    
  elif v=="Thor":
    if poder=="Martelo":
      if energia>=4:
        print("Thor conseguiu derrotar Thanos");
      elif energia<4:
        print("Thor NAO conseguiu derrotar Thanos, chamem outro Vingador");
            
    elif poder=="Armadura de Ferro":
      print("Thor NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Homem de Ferro");
      
    elif poder== "Escudo":
      print("Thor NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Capitão América");
      
    elif poder== "Força Bruta":
      print("Thor NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Hulk");
      
    elif poder== "Arco e Flecha":
      print("Thor NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Gavião Arqueiro");
      
    elif poder== "Inteligência":
      print("Thor NAO conseguiu derrotar Thanos");
      print("Esse é o poder da Viúva Negra");

  elif v=="Gavião Arqueiro":
    if poder=="Arco e Flecha":
      if energia>=12:
        print("Gavião Arqueiro conseguiu derrotar Thanos");
      elif energia<12:
        print("Gavião Arqueiro NAO conseguiu derrotar Thanos, chamem outro Vingador");
            
    elif poder=="Armadura de Ferro":
      print("Gavião Arqueiro NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Homem de Ferro");
      
    elif poder== "Escudo":
      print("Gavião Arqueiro NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Capitão América");
      
    elif poder== "Força Bruta":
      print("Gavião Arqueiro NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Hulk");
      
    elif poder== "Martelo":
      print("Gavião Arqueiro NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Thor");
      
    elif poder=="Inteligência":
      print("Gavião Arqueiro NAO conseguiu derrotar Thanos");
      print("Esse é o poder da Viúva Negra");

  elif v=="Viúva Negra":
    if poder=="Inteligência":
      if energia>=20:
        print("Viúva Negra conseguiu derrotar Thanos");
      elif energia<20:
        print("Viúva Negra NAO conseguiu derrotar Thanos, chamem outro Vingador");
            
    elif poder=="Armadura de Ferro":
      print("Viúva Negra NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Homem de Ferro");
      
    elif poder== "Escudo":
      print("Viúva Negra NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Capitão América");
      
    elif poder== "Força Bruta":
      print("Viúva Negra NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Hulk");
      
    elif poder== "Martelo":
      print("Viúva Negra NAO conseguiu derrotar Thanos");
      print("Esse é o poder do Thor");
      
    elif poder=="Arco e Flecha":
      print("Viúva Negra NAO conseguiu derrotar Thanos");
      print("Esse é o poder da Viúva Gavião Arqueiro");
     
else:
  print("Vingador Inválido");



