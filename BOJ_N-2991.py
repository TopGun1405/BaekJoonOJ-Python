def main():
    A, B, C, D = map(int, input().split())
    PMN = list(map(int, input().split()))
    for m in PMN:
        dogAttack = 0
        if 0 < m % (A + B) <= A:
            dogAttack += 1
        if 0 < m % (C + D) <= C:
            dogAttack += 1
        print(dogAttack)


if __name__ == "__main__":
    main()
