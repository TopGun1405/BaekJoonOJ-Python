def main():
    n, A = map(int, input().split())
    a = list(map(int, input().split()))

    ticket = 0
    for ai in a:
        ticket += ai // A
    print(ticket)


if __name__ == "__main__":
    main()
