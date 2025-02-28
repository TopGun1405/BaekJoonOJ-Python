def main():
    T = int(input())

    for x in range(1, T+1):
        G, M, D = input().split()

        feet_M, inches_M = map(int, M.strip('"').split("'"))
        feet_D, inches_D = map(int, D.strip('"').split("'"))

        m = feet_M * 12 + inches_M
        d = feet_D * 12 + inches_D
        md = m + d + (5 if G == "B" else -5)

        odd = md & 1
        md //= 2
        A, B = md - (3 if odd else 4), md + 4

        print(f"Case #{x}: {A // 12}'{A % 12}\" to {B // 12}'{B % 12}\"")


if __name__ == "__main__":
    main()
