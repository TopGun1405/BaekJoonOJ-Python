def main():
    P, K = map(int, input().split())
    for n in range(2, K):
        if P % n == 0:
            print("BAD", n)
            break
    else:
        print("GOOD")


if __name__ == "__main__":
    main()
