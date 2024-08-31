def main():
    n = int(input())
    way = list(input())

    cnt = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    for c in way:
        cnt[c] += 1

    print(n - max(cnt.values()))


if __name__ == "__main__":
    main()
