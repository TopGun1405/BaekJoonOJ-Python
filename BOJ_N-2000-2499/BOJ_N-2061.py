def main():
    K, L = map(int, input().split())
    for i in range(2, L):
        if K % i == 0:
            print("BAD", i)
            break
    else:
        print("GOOD")


if __name__ == "__main__":
    main()
