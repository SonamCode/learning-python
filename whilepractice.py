"""i = 1
while i <= 100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1

n =int(input("enter the number"))5

i=1
while i<=10:
    print(n*i)
    i +=1

num = [1,34,56,78,99,33,56,478,89,69]

i = 0
while i<len(num):
    print(num[i])
    i +=1"""

num = [1,34,56,78,99,33,56,478,89,69]
x=33
i=0
while i<len(num):
    if(num[i] == x):
        print("found indx" ,i)
        break
    else:
        print("finding..")
    i +=1