def main():
    N = int(input())

    min_num, max_num, tot = 1e10, 0, 0
    for _ in range(N):
        a_i, b_i = map(int, input().split())
        k = a_i / b_i
        min_num, max_num = min(min_num, k), max(max_num, k)
        tot += k

    print(f"{min_num:.6f} {max_num:.6f} {tot:.6f}")


if __name__ == "__main__":
    main()
