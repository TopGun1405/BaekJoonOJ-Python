def main():
    stroke_Cnt = {'j': 2, 'o': 1, 'i': 2}

    N = int(input())
    S = input()

    cnt = 0
    for c in S:
        cnt += stroke_Cnt[c]

    print(cnt)


if __name__ == "__main__":
    main()
