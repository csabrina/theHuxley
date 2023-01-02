number= int(input());

if(1<=number<=40):
  for i in range(1, number+1):
    for j in range(1,i+1):
        if(i==j):
            print(j, end="");
        else:
            print(j, end=" ");
    print();
   