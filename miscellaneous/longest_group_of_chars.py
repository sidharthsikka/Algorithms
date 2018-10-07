def longest(line):
    max_count = 0
    max_char = ''
    if len(line) > 0:
        prev = line[0]
        c_count = 1
        for i in range(1,len(line)):
            c = line[i]
            if prev == c:
                c_count+=1
                if c_count > max_count:
                    max_char = c
                    max_count = c_count
            else:
                prev = c
                c_count = 1
    return max_char + str(max_count)

def main():
    print(longest("aabbbaabaa"))

main()    

