from itertools  import combinations
l=[15,20,15,13,200,7,19,5]
p=220
f=list(combinations(l,2))
print(f)
for x in f:
    if(sum(x)==p):
        print(x)