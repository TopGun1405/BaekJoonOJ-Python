def main():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print("Case {}: {}".format(i + 1, a + b))


if __name__ == "__main__":
    main()
