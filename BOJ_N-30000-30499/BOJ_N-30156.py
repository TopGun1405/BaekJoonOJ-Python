def main():
    T = int(input())
    for _ in range(T):
        s = input()

        cnt = {}
        for c in s:
            try:
                cnt[c] += 1
            except KeyError:
                cnt[c] = 1

        print(min(cnt.values()) if len(cnt.keys()) > 1 else 0)


if __name__ == "__main__":
    main()
