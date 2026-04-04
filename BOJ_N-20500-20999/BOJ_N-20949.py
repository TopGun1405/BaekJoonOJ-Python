def main():
    N = int(input())
    Monitor = [list(map(int, input().split())) + [i+1] for i in range(N)]
    Monitor.sort(key=lambda k: (k[0]**2 + k[1]**2), reverse=True)

    for i in range(N):
        print(Monitor[i][2])


if __name__ == "__main__":
    main()
