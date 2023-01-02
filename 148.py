def gap(text):
  count=0
  for i in range(0,len(text)):
    if text [i] == "A" or text [i] =="D" or text [i] == "O" or text [i] == "P" or text [i] =="R" or text [i] =="Q":
      count+=1
    elif text[i] == "B":
      count+=2
  return count


test= int(input())

for x in range(test):
  text= input().upper()
  print(gap(text))

