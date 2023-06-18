def main():
    K = int(input())
    s = input()
    for i in range(0, len(s), K):
        print(s[i], end='')


if __name__ == "__main__":
    main()
