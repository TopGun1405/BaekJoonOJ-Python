def main():
    N = int(input())
    S = input()

    print("Yes" if S.count("O") >= N / 2 else "No")


if __name__ == "__main__":
    main()
