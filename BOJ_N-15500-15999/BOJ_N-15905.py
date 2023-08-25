def main():
    N = int(input())
    p_info = [list(map(int, input().split())) for _ in range(N)]
    p_info.sort(key=lambda k: (-k[0], k[1]))
    print(len(list(filter(lambda n: n[0] == p_info[4][0], p_info[5:]))))


if __name__ == "__main__":
    main()
