a = ['foo' , 'bar' ,'baz','qux','corge']
s = 'ps4'
i = 0
while i < len  (a):
    if a[i] == s:
        #Processing for item found
        break
        
    i+=1
else:
    #Processing for item not found
    print(s,'is found in list.')
