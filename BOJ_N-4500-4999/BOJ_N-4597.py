def main():
    while True:
        n = input()
        if n == '#':
            break
        if n[-1] == 'e':
            print(n[:-1] + ('1' if n.count('1') % 2 else '0'))
        elif n[-1] == 'o':
            print(n[:-1] + ('0' if n.count('1') % 2 else '1'))


if __name__ == "__main__":
    main()
