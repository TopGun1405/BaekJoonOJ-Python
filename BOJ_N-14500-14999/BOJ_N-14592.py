def main():
    N = int(input())
    part = [list(map(int, input().split())) + [i + 1] for i in range(N)]
    part.sort(key=lambda k: (-k[0], k[1], k[2]))
    print(part[0][3])


if __name__ == "__main__":
    main()
