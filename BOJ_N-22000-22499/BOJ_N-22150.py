def main():
    t = int(input())
    for _ in range(t):
        c = list(map(int, input().split()))
        n, chocolate = c[0], c[1:]
        for l_i, r_i in zip(chocolate[::2], chocolate[1::2]):
            if l_i + r_i != n:
                print("yes")
                break
        else:
            print("no")


if __name__ == "__main__":
    main()
