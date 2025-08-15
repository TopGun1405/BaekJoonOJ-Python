def main():
    n = int(input())
    selected = {}
    for _ in range(n):
        strings = input().split()
        n, apps = strings[0], strings[1:]

        for app in apps:
            if app in selected:
                continue
            selected[app] = True
            break

    print(*selected.keys())


if __name__ == "__main__":
    main()
