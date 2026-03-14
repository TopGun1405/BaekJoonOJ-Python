def main():
    n = int(input())
    x = [int(input()) for _ in range(n)]

    min_energy = int(1e9)
    for i in range(n):
        for j in range(i+1, n):
            a, b = x[i], x[j]
            total_energy = 0
            for k in range(n):
                if k == i or k == j:
                    continue
                c = x[k]
                total_energy += min((a-c)**2, (b-c)**2)

            min_energy = min(min_energy, total_energy)

    print(min_energy)


if __name__ == "__main__":
    main()
