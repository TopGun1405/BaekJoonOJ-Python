def main():
    D = list(map(int, input().split()))

    print(len(set(range(1, 5)) - set(D)))


if __name__ == "__main__":
    main()
