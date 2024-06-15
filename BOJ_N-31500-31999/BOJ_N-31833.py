def main():
    N = int(input())
    A = input().split()
    B = input().split()

    print(min(int("".join(A)), int("".join(B))))


if __name__ == "__main__":
    main()
