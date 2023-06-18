def main():
    N, p = int(input()), int(input())
    if N <= 5:
        for _ in range(N - 1):
            p = int(not p)
            print(p)
    else:
        print("Love is open door")


if __name__ == "__main__":
    main()
