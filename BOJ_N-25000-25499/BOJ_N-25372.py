def main():
    N = int(input())
    for _ in range(N):
        pw = input()
        print("yes" if 6 <= len(pw) <= 9 else "no")


if __name__ == "__main__":
    main()
