def main():
    T = int(input())
    cube = [n ** 3 for n in range(1500) if n ** 3 < 2_000_000_000]
    for t in range(T):
        A, B = map(int, input().split())
        print("Case #{}: {}".format(t + 1, len(list(filter(lambda n: A <= n <= B, cube)))))


if __name__ == "__main__":
    main()
