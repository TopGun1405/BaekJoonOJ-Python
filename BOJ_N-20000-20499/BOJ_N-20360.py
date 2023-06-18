def main():
    n = bin(int(input()))[2:][::-1]
    i = 0
    while i < len(n):
        if n.find('1', i) == -1:
            break
        print(n.find('1', i), end=' ')
        i = n.find('1', i) + 1


if __name__ == "__main__":
    main()
