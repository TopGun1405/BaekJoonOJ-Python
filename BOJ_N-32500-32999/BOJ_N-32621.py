def main():
    S = input()

    s = S.split("+")
    if len(s) != 2:
        print("No Money")
    elif len(set(s)) != 1 or s[0].startswith("0"):
        print("No Money")
    else:
        for c in s:
            if not c.isdigit():
                print("No Money")
                break
        else:
            print("CUTE")


if __name__ == "__main__":
    main()
