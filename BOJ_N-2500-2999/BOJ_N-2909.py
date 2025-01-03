def main():
    C, K = map(int, input().split())
    print(int(round(C + 0.1, -K)))


if __name__ == "__main__":
    main()
