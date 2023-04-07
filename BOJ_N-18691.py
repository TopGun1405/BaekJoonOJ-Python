def main():
    T = int(input())
    for _ in range(T):
        G, C, E = map(int, input().split())
        group = [lambda p: p, lambda p: p*3, lambda p: p*5]
        print(group[G-1](E-C) if E - C >= 0 else 0)


if __name__ == "__main__":
    main()
