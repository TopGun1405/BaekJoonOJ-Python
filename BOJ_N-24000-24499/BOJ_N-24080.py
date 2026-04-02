def main():
    N = int(input())
    S = input()

    print("Yes" if len(set(S)) >= 3 else "No")


if __name__ == "__main__":
    main()
