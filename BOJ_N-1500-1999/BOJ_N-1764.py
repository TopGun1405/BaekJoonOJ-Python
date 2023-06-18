def main():
    nh, ns = map(int, input().split())
    nhl = {input() for _ in range(nh)}
    nsl = {input() for _ in range(ns)}

    nhs = sorted(nhl & nsl)
    print(len(nhs))
    print(*nhs, sep='\n')


if __name__ == "__main__":
    main()
