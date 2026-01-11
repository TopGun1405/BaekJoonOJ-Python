def main():
    N = int(input())
    d = {'R': 0.55, 'G': 0.7, 'B': 0.8, 'Y': 0.85, 'O': 0.9, 'W': 0.95}
    for _ in range(N):
        p = list(map(lambda e: e if e.isalpha() else float(e), input().split()))

        cost, dot, coupon, pay = p
        cost *= d[dot]
        cost *= 0.95 if coupon == "C" else 1

        if pay == "P":
            print(f"${cost:.2f}")
        else:
            cost = int(cost * 100)
            cost = (cost + 10 - cost % 10) if cost % 10 > 5 else (cost - cost % 10)

            print(f"${cost/100:.2f}")


if __name__ == "__main__":
    main()
