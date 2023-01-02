number= int(input());

if(1<=number<=30):
  for i in range(1, number+1):
    for j in range(1,i+1):
      print(i, end="");
    print();