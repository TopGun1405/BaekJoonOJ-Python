def main():
    n = int(input())
    a = input().split()

    for i in range(n):
        for j in range(n):
            if a[i].startswith(a[j]):
                print(i+1, j+1)
                exit()
    print(-1)


if __name__ == "__main__":
    main()
