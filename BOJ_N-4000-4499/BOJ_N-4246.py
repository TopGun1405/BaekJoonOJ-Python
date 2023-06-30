def main():
    while True:
        n = int(input())
        if n == 0:
            break
        text = input()

        S = []
        for i in range(len(text) // n):
            S.append(text[n*i:n*(i+1)][::-1] if i % 2 else text[n*i:n*(i+1)])

        for s in zip(*S):
            print(''.join(s), end='')
        print()


if __name__ == "__main__":
    main()
