def main():
    N = int(input())
    a = input()
    for ai, aj in zip(a[:-2:2], a[2::2]):
        if ai != aj:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
