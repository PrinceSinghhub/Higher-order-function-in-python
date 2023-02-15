from numpy import *
n=['1','20','30']
# i want to convert all str elemrnt in int
for i in range(len(n)):
    print(int(n[i]))
# here we apply map
a=list(map(int,n))
b=array(a)
print(b)
print(a)