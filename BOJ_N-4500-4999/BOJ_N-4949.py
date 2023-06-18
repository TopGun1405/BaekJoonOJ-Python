def main():
    while True:
        S = input()
        if S == '.':
            break

        stack = []
        for s in S:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    print("no")
                    break
            elif s == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    print("no")
                    break
        else:
            print("yes" if len(stack) == 0 else "no")


if __name__ == "__main__":
    main()
