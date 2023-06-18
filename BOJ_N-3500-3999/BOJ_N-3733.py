def main():
    while True:
        try:
            N, S = map(int, input().split())
            print(S // (N + 1))
        except:
            break


if __name__ == "__main__":
    main()
