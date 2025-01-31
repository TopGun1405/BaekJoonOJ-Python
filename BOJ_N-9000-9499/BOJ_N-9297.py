def main():
    t = int(input())
    for x in range(1, t+1):
        n, d = map(int, input().split())

        print(f"Case {x}: ", end="")
        nd, dn = n // d, n % d
        if nd != 0 and dn != 0:
            print(f"{nd} {dn}/{d}")
        elif nd == 0 and dn != 0:
            print(f"{dn}/{d}")
        elif nd != 0 and dn == 0:
            print(f"{nd}")
        else:
            print(0)


if __name__ == "__main__":
    main()
