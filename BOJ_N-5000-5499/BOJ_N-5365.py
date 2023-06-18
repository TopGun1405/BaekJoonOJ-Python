def main():
    n = int(input())
    S = input().split()
    decode, idx = [], 0
    for s in S:
        if len(s) > idx:
            decode.append(s[idx])
        else:
            decode.append(' ')
        idx = len(s) - 1
    print(''.join(decode))


if __name__ == "__main__":
    main()
