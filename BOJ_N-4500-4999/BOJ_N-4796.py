def main():
    t = 1
    while True:
        L, P, V = map(int, input().split())
        if L == P == V == 0:
            break
        print(f"Case {t}: {V // P * L + min(V % P, L)}")
        t += 1


if __name__ == "__main__":
    main()
