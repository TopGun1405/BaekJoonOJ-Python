def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        mem = input().split()
        rem = input().split()

        if mem == rem or sorted(mem) == sorted(rem):
            print("NOT CHEATER")
        else:
            print("CHEATER")


if __name__ == "__main__":
    main()
