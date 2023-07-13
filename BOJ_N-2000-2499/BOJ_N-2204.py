def main():
    while True:
        n = int(input())
        if n == 0:
            break
        words = sorted([input() for _ in range(n)], key=lambda k: k.lower())
        print(words[0])


if __name__ == "__main__":
    main()
