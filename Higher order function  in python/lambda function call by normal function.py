def pr():
    x=20
    # lambda function call by normal function
    return (lambda y:x+y)
p=pr()
print(p(10))