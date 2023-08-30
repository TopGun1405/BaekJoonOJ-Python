def main():
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        v1 = sorted(map(int, input().split()))
        v2 = sorted(map(int, input().split()), reverse=True)
        print(f"Case #{t}: {sum(map(lambda v: v[0] * v[1], zip(v1, v2)))}")


if __name__ == "__main__":
    main()
