a=['foo','bar','baz','qux']
s='corge'
i=0
try:
    print (a.index ('corage'))
except ValueError:
    print (s,'not found in list')
