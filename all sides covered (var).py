n=input()
count = 0
count1 = 0
count2 = 0
for i in n:
    if(i == '['):
        count = count + 1
    elif(i == ']'):
        count = count - 1
    elif(i == '('):
        count1 = count1 + 1
    elif(i == ')'): 
        count1 = count1 - 1
    elif(i == '{'):
        count2 = count2 + 1
    elif(i== '}'):
        count2 = count2 - 1
        
if(count == 0 and count1==0 and count2==0):
    print("true")
else:
    print("false")