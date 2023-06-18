def main():
    N, S = int(input()), input()
    ans = 0
    for s in S:
        if s in ['a', 'e', 'i', 'o', 'u']:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
