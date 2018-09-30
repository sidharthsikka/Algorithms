def evaluate_reverse_polish_notation(tokens):
    stack = []
    def eval(first,second,operator):
        print(first, operator, second)
        if operator == "+":
            return first + second
        elif operator == "-":
            return first - second
        elif operator == "*":
            return first * second
        return int(first/second)
    for i in tokens:
        if i == "+" or i == "-" or i == "*" or i == "/":
            second = stack.pop()
            first = stack.pop()
            result = eval(first, second, i)
            print(result)
            stack.append(result)
        else:
            stack.append(int(i))
    return stack.pop()

def main():
    res = evaluate_reverse_polish_notation(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])
    print(res)

main()