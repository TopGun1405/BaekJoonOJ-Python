def main():
    N = int(input())
    lectures = list(map(int, input().split()))
    create, miss = 0, 0
    before = lectures[0]
    for lecture in lectures:
        if lecture > before:
            miss += lecture - before
        elif lecture < before:
            create += before - lecture
        before = lecture
    print(create, miss)


if __name__ == "__main__":
    main()
