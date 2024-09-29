def main():
    N, A, B = map(int, input().split())

    o1, o2 = 1, 1
    role = True
    for _ in range(N):
        o1 += A if role else B
        o2 += B if role else A

        if role and o2 > o1:
            role = False
        if not role and o1 > o2:
            role = True

        if o1 == o2:
            if role:
                o2 -= 1
            else:
                o1 -= 1

    print(f"{o1 if role else o2} {o2 if role else o1}")


if __name__ == "__main__":
    main()
