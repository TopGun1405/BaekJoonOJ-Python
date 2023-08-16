def main():
    n = int(input())
    a = list(map(int, input().split()))

    e = list(filter(lambda k: k % 2 == 0, a))
    print("Happy" if len(e) * 2 > n else "Sad")


if __name__ == "__main__":
    main()
