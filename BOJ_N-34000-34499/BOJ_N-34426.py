def main():
    num_legs = int(input())
    res = []
    for _ in range(num_legs):
        num_routes = int(input())
        route = list(map(int, input().split()))

        min_time = float("inf")
        best_route = -1
        for i in range(num_routes):
            s, d = route[i*2], route[i*2 + 1]
            t = d / s

            if t < min_time:
                min_time = t
                best_route = i+1

        res.append(best_route)

    print(*res, sep="\n")


if __name__ == "__main__":
    main()
