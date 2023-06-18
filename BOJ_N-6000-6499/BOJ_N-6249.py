def main():
    n, p, h = map(int, input().split())
    for _ in range(n):
        dollar = int(input())
        if dollar > h:
            print("BBTV: Dollar reached {} Oshloobs, A record!".format(dollar))
            h = p = dollar
            continue
        if dollar < p:
            print("NTV: Dollar dropped by {} Oshloobs".format(p - dollar))
        p = dollar


if __name__ == "__main__":
    main()
