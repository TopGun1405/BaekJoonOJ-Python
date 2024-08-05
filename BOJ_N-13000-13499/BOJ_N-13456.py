def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        v = list(map(int, input().split()))
        u = list(map(int, input().split()))

        hDis = 0
        for v_n, u_n in zip(v, u):
            if v_n != u_n:
                hDis += 1

        print(hDis)


if __name__ == "__main__":
    main()
