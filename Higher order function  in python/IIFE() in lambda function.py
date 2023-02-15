#normal lambda fuction
pr=lambda x,y:x+y
print(pr(5,2))
# apply IIFE(immeditely invoked function experession)
a=(lambda x,y:x+y)(5,2)
print(a)