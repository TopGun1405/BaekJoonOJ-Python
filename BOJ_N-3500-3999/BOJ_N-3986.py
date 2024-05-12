def main():
    N = int(input())

    goodWord = 0
    for _ in range(N):
        word = list(input())

        stack = []
        for c in word:
            if stack and stack[-1] == c:
                stack.pop(-1)
            else:
                stack.append(c)

        if not stack:
            goodWord += 1

    print(goodWord)


if __name__ == "__main__":
    main()
