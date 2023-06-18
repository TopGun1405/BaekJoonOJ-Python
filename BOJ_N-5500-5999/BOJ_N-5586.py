def main():
    s = input()
    i, joi, ioi = 0, 0, 0
    while i < len(s):
        if s[i:i + 3] == 'JOI':
            joi += 1
            i += 2
        elif s[i:i + 3] == 'IOI':
            ioi += 1
            i += 2
        else:
            i += 1
    print(joi)
    print(ioi)


if __name__ == "__main__":
    main()
