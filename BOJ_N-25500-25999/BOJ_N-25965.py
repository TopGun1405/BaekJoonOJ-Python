def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        missions = [list(map(int, input().split())) for _ in range(M)]
        K, D, A = map(int, input().split())
        donation = 0
        for mission in missions:
            calc = mission[0] * K - mission[1] * D + mission[2] * A
            donation += calc if calc > 0 else 0
        print(donation)


if __name__ == "__main__":
    main()
