def square(n):

    temp=0
    for i in range(len(n)):
        curr=n[i]
        temp=temp+(int(curr)*int(curr))
    return str(temp)
def check(n):
    s=set()
    while n!="1" and n not in s:
        s.add(n)
        n=square(n)
    if n=="1":
        return "true"
    else:
        return "false"

print(check(input()))