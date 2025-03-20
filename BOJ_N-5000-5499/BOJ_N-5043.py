def main():
    N, b = map(int, input().split())
    print("yes" if N < 2**(b+1) else "no")


if __name__ == "__main__":
    main()
