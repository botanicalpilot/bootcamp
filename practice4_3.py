import string

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

letters = list(string.ascii_lowercase)

for item in letters:
    for key in d:
        butt = dict(item)
        if key.startswith(item, 0 , 2):
            print(d.viewkeys())


'''
need to figure out how to get values for each letter:

'''