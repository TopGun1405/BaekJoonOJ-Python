def main():
    X = list(map(int, list(input())))
    count = 0
    while True:
        if len(X) == 1:
            break
        X = list(map(int, list(str(sum(X)))))
        count += 1
    print(count)
    print("YES" if X[0] % 3 == 0 else "NO")


if __name__ == "__main__":
    main()
