def main():
    N = int(input())

    for r in range(N):
        for c in range(N):
            if r == 0 or r == N-1 or c == 0 or c == N-1:
                print("*", end="")
            elif r == c or r + c == N-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
