def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    for i, Ai in enumerate(A):
        print(len([Aj for Aj in A[:i] if Aj < Ai]))


if __name__ == "__main__":
    main()
