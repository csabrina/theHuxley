primeiraDose= int(input());
periodicidade= int(input()); 

for i in range(3):
  print(primeiraDose+periodicidade, end=" ");
  primeiraDose+=periodicidade; 