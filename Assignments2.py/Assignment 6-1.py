#5-1
import random
def sumProduct(l1, l2):
  if len(l1) != len(l2):
    print('The length is not the same')
    quit()
  product = []
  for i in range (0, len(l1)):
    product.append(l1[i]*l2[i])
  return sum(product)

lst1 = []
for i in range (int(input('Enter list length'))):
  s = random.randint(0,10)
  lst1.append(s)
print(lst1)

lst2 = []
for i in range (int(input('Enter list length'))):
  s = random.randint(0,10)
  lst2.append(s)
print(lst2)


products=sumProduct(lst1, lst2)
print(products)

#5-2
def stripspace(stri):
  uppercase = ''
  for letter in stri:
        if letter.isupper():
          uppercase += letter  
  return uppercase

if __name__ == '__main__':
  message = input("Enter message")
  stripspace(message)
  let = stripspace(message)
  print(let)
