import random
i = 0;

while True:
  n = random.randint(0,100)
  print(n)
  i += n
  if (i<100):
    break
    print (i, end=',')
print ("The Sum is", i-n)
