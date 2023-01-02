n = int(input())
num_triangular = 0
for i in range(1, n+1):
    if i * (i+1) * (i+2) == n:
      print("{} * {} * {} = {}".format(i, (i+1), (i+2), n))
      print("Verdadeiro")
      num_triangular += 1
if n <= 0 or num_triangular < 1:
  print("Falso")
