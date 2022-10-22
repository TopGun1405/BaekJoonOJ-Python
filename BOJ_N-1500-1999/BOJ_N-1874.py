def main():
    n = int(input())
    c = 1
    isValid = True
    stack, op = [], []

    for i in range(n):
        num = int(input())
        while c <= num:
            stack.append(c)
            op.append('+')
            c += 1
        if stack[-1] == num:
            stack.pop()
            op.append('-')
        else:
            isValid = False

    if not isValid:
        print("NO")
    else:
        print(*op, sep='\n')


if __name__ == "__main__":
    main()
