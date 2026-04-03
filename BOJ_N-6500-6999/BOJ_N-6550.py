def main():
    while True:
        try:
            s, t = map(list, input().split())

            i, sub = 0, False
            for c in t:
                if s[i] == c:
                    i += 1
                    if i == len(s):
                        sub = True
                        break

            if sub:
                print("Yes")
            else:
                print("No")

        except EOFError:
            break


if __name__ == "__main__":
    main()
