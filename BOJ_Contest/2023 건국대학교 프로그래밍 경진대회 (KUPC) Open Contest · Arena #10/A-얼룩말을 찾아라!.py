def main():
    N, L = map(int, input().split())
    pattern = []
    for _ in range(N):
        pattern.append(list(filter(lambda e: e.isdigit(), input().split('0'))))
    cnt = list(map(lambda e: len(e), pattern))
    print(max(cnt), cnt.count(max(cnt)))


if __name__ == "__main__":
    main()
