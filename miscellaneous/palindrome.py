def palindrome(s):
    def isAlpha(c):
        if 'a' <= c and c <= 'z' or '0' <= c and c <= '9':
            return True
        return False
    s = s.lower()
    line = ""
    for i in s:
        if isAlpha(i):
            line = line + i
    reverse = line[::-1]
    return reverse == line

def main():
    print(palindrome("hesteeh"))

main()    