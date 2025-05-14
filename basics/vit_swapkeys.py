D={'a':10, 'b': 20, 'c':30}
k=list(D.keys())
i=0
while i<len(D):
    D.update({D[k[i]]:k[i]})
    del D[k[i]]
    i=i+1
print(D)
