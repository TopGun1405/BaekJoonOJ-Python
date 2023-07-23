def main():
    k = int(input())
    w = int(input())
    h = int(input())
    t = int(input())

    for _ in range(t):
        print('*' * (w * k + t * (w + 1)))

    for _ in range(h):
        for _ in range(k):
            for _ in range(w):
                print('*' * t + '.' * k, end='')
            print('*' * t)
        for _ in range(t):
            print('*' * (w * k + t * (w + 1)))


if __name__ == "__main__":
    main()
