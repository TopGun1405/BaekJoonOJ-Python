def main():
    T = int(input())
    for _ in range(T):
        G = int(input())
        nums = [int(input()) for _ in range(G)]
        m = 0
        while True:
            m += 1
            if len(set(map(lambda n: n % m, nums))) == G:
                print(m)
                break


if __name__ == "__main__":
    main()
