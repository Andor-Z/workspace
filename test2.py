a={'a':1,'b':2,'c':3};b=a.copy()
for k in a.keys():
    if a[k]>2:
        del b[k]
print(b)