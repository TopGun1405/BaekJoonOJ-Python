def main():
    N, S = map(lambda e: int(e) if e.isdigit() else e, input().split())

    items, removed = {}, 0
    for _ in range(N):
        names, cnt = map(lambda e: int(e) if e.isdigit() else e, input().split())

        if S in names.split("_"):
            removed += cnt

    print(removed)


if __name__ == "__main__":
    main()
