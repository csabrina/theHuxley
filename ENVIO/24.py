while True:
  n= int(input())
  if n == -1:
      break
  elif 0<=n<=12:
      fatorial= 1
      for i in range(1, n+1):
        fatorial *=i
  print(fatorial)
