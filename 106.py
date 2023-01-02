while True:
    n= int(input());
    if n==0:
        break
    else:
        a=0
        b=1
        c=1
        for i in range(n):
          if i!= n-1:
              print(a, end=" ")
          else:
              print(a, end="\n")
          c= a+b
          a=b
          b=c