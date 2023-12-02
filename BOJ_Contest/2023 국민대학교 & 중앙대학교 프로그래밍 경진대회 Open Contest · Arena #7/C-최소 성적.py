def main() -> None:
    grades = {
        "A+": 4.50,
        "A0": 4.00,
        "B+": 3.50,
        "B0": 3.00,
        "C+": 2.50,
        "C0": 2.00,
        "D+": 1.50,
        "D0": 1.00,
        'F': 0.00
    }
    N, X = map(float, input().split())
    tot_c, tot_c_g = 0, 0
    for _ in range(int(N) - 1):
        ci, gi = input().split()
        tot_c += int(ci)
        tot_c_g += int(ci) * grades[gi]
    L = int(input())
    tot_c += L

    print(tot_c, tot_c_g)


if __name__ == "__main__":
    main()
