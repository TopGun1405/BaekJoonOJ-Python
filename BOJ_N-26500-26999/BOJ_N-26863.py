def main():
    a = sorted(int(input()) for _ in range(4))
    b = int(input())

    if a[0] == a[1] == a[2] == a[3]:
        print(1)
    elif a[0] + b == a[1] == a[2] == a[3]:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
