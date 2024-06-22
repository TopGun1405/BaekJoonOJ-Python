def main():
    N, X = map(int, input().split())
    bus = []
    for _ in range(N):
        S, T = map(int, input().split())
        # if S + T <= X:
        #     bus.append(S)
        bus.append([S, T, S+T])

    bus = list(filter(lambda n: n[2] <= X, bus))

    # print(sorted(bus)[-1] if bus else -1)
    print(sorted(bus, key=lambda k: k[0])[-1][0] if bus else -1)


if __name__ == "__main__":
    main()
