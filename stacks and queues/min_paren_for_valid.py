def minAddToMakeValid(s):
    stack = []
    for i in s:
        if i == ")":
            if len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return len(stack)