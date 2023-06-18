def main():
    while True:
        a, b = map(int, input().split())
        if not a:
            break
        print("Yes" if a > b else "No")


if __name__ == "__main__":
    main()
