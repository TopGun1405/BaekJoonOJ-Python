def main():
    T = int(input())
    for x in range(1, T+1):
        N = int(input())

        for n in range(N, -1, -1):
            if str(n) == "".join(sorted(str(n))):
                print(f"Case #{x}: {n}")
                break


if __name__ == "__main__":
    main()
