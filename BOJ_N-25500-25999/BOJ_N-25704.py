def main():
    N = int(input())
    P = int(input())
    pay = [P]
    if N >= 5:
        pay.append(max(P - 500, 0))
    if N >= 10:
        pay.append(int(P * 0.9))
    if N >= 15:
        pay.append(max(P - 2000, 0))
    if N >= 20:
        pay.append(int(P * 0.75))
    print(min(pay))


if __name__ == "__main__":
    main()
