def main():
    K = int(input())
    for x in range(1, K+1):
        A, E = map(int, input().split())

        if E >= A:
            res = "no drought"
        else:
            mega, k = A / E, 0
            while mega > 1:
                k += 1
                mega /= 5
            res = "mega " * (k-1) + "drought"

        print(f"Data Set {x}:")
        print(res)
        print()


if __name__ == "__main__":
    main()
