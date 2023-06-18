def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        print("Case {}:".format(t + 1))
        for n in range(1, 7):
            for m in range(n, 7):
                if n + m == N:
                    print("({},{})".format(n, m))


if __name__ == "__main__":
    main()
