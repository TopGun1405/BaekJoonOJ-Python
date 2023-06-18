def main():
    T = int(input())
    for _ in range(T):
        message, rule = input(), input()
        for c in message:
            print(rule[ord(c) - 65], end='') if c != ' ' else print(c, end='')
        print()


if __name__ == "__main__":
    main()
