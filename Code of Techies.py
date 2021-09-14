def check(n):
    n=int(n)
    n=abs(n)
    n=str(n)
    i,j=0,len(n)-1
    while i<=j:
        if n[i]!=n[j]:
            return "false"
        i+=1
        j-=1
    return "true"
    
print(check(input()))
    