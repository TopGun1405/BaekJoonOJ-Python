def main():
    n = int(input())
    s = input()
    yee = {'2': 0, 'e': 0}
    for c in s:
        yee[c] += 1
    print(2 if yee['2'] > yee['e']
          else ('e' if yee['e'] > yee['2']
                else "yee"))


if __name__ == "__main__":
    main()
