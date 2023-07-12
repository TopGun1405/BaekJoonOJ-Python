def main():
    S, E = map(int, input().split())

    for n in range(S, E + 1):
        n = str(n)
        print("Palindrome!" if n == n[::-1] else n)


if __name__ == "__main__":
    main()
