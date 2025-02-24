def main():
    S = input()
    bomb = input()

    stack = []
    for c in S:
        stack.append(c)
        if len(stack) >= len(bomb) and "".join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

    print("".join(stack) if stack else "FRULA")


if __name__ == "__main__":
    main()
