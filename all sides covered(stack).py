def check(n):
    stack=[]
    for i in range(len(n)):
        curr=n[i]
        if curr=="{" or curr=="(" or curr=="[":
            stack.append(curr)
        elif stack:
            if curr==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return "false"
            elif curr=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return "false"
            elif curr=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return "false"
        else:
            return "false"
    if stack:
        return "false"
    else:
        return "true"
                
    
print(check(input()))