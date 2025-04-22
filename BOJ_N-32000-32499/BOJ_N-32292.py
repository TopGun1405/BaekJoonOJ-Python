def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = input()

        while "ABB" in S:
            S = S.replace("ABB", "BA")

        print(S)


if __name__ == "__main__":
    main()
