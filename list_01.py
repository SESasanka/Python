a = ['foo','bar']
while len(a):
    print(a.pop(0))
    b = ['baz','qux']
    while len(b):
        print('>',b.pop(0))
