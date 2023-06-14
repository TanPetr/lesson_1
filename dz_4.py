def palindrom(s):
    k=0
    for i in range (1,len(s)//2 +1):
        if s[i-1] == s[-i]:
            k+=1
    if k == len(s)//2:
        print('True')
    else:
        print('False')

palindrom('lkl')
palindrom('helloword')
        
