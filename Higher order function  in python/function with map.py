def pr(a):
    return a*a
def codex(a):
    return a*a*a
p=[pr,codex]
for i in range(5):
    r=list(map(lambda v:v(i),p))
    print(r)