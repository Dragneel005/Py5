U=int(input('Input number of scores'))
Bill=[]
for i in range (U):
  bill=int(input("Enter Bill's scores"))
  Bill.append(bill)

Jim=[]
for i in range (U):
  jim=int(input("Enter Jim's scores"))
  Jim.append(jim)

Joe=[]
for i in range (U):
  joe=int(input("Enter Joe's scores"))
  Joe.append(joe)
  
n=Joe, Jim, Bill
na=[n]
  
list2d =[]
for i in range(3):
  name = []
  for j in range(U):
    na.append(int(input("Enter {}'s score: ".format(na[i]))))
  list2d.append(name)

print('Bill=',Bill)
print('Jim= ',Jim)
print('Joe= ',Joe)


x=sum(Bill)
y=x/len(Bill)
print("The sumation of Bill's score is=",x )
print("The average of Bill's scores is=", y)


a=sum(Jim)
s=a/len(Jim)
print("The sumation of Jim's score is=",a )
print("The average of Jim's scores is=", s)


d=sum(Joe)
f=d/len(Joe)
print("The sumation of Joe's score is=",d )
print("The average of Joe's scores is=", f)
