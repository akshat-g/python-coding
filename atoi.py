
def atoi(string):
    sign = 1 # for positive numbers
    res = 0
    i = 0

    if string[0] == "-":
        sign = -1
        i = 1

    for j in range(i, len(string)):
        res = res * 10 + (ord(string[j]) - ord('0'))

    return sign * res

if __name__ == "__main__":
    string = "-123"
    print atoi(string)
