def main():
    N = int(input())
    text = input().split()
    shock = 0
    for c in text:
        if c == "he" or c == "him" or c == "she" or c == "her":
            shock += 1
    print(shock)


if __name__ == "__main__":
    main()
