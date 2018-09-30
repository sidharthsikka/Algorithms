def balanced_brackets(line):
    stack = []
    open_brackets = ['(','{','[']
    close_brackets = [')','}',']']
    for i in line:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            temp = stack.pop()
            if close_brackets.index(i) != open_brackets.index(temp):
                return False
    if len(stack) == 0:
        return True
    return False


def main():
    print(balanced_brackets("{(TE[S}]T)"))

main()
