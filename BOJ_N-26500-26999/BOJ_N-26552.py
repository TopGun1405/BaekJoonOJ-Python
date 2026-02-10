def main():
    n = int(input())
    for _ in range(n):
        k = int(input())
        while True:
            k += 1
            if "0" not in str(k):
                print(k)
                break


if __name__ == "__main__":
    main()
