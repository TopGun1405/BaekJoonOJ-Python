def main():
    k, s = map(int, input().split())

    print((s // k) + (s % k))


if __name__ == "__main__":
    main()
