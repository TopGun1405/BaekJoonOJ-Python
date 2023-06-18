def main():
    n = int(input())
    # list is slow
    rec = set()
    for _ in range(n):
        name, log = input().split()
        if log == 'enter':
            rec.add(name)
        elif log == 'leave':
            rec.remove(name)
    print(*sorted(rec, reverse=True), sep='\n')


if __name__ == "__main__":
    main()
