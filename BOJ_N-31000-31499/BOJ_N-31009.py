def main():
    N = int(input())
    info = {}
    for _ in range(N):
        Di, Ci = map(lambda e: int(e) if e.isdigit() else e, input().split())
        info[Di] = Ci

    jinju = info['jinju']
    print(jinju)
    print(len(list(filter(lambda cost: cost > jinju, info.values()))))


if __name__ == "__main__":
    main()
