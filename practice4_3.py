import string

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

def averageDict(d):
    a = [v for k, v in d.items() if k.startswith('a')]
    b = [v for k, v in d.items() if k.startswith('b')]
    c = [v for k, v in d.items() if k.startswith('c')]
    newdict = {'a': (sum(a)/len(a)), 'b': (sum(b)/len(b)), 'c': (sum(c)/len(c))}
    return newdict

print(averageDict(d))

        
    