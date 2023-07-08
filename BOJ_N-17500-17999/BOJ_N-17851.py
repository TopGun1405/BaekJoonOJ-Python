def main():
    h1 = sorted(map(int, input().split()))
    h2 = sorted(map(int, input().split()))
    h = list(filter(lambda n: n[0] > n[1], zip(h1, h2)))
    print(len(h))


if __name__ == "__main__":
    main()
