def main():
    CH, CM, CS = map(int, input().split(":"))
    SH, SM, SS = map(int, input().split(":"))
    t, k = map(int, input().split())

    S1 = CH*3600 + CM*60 + CS
    S2 = SH*3600 + SM*60 + SS

    if S1 > S2:
        print(0)
    else:
        print(1 if t * (100 - k) / 100 <= S2 - S1 else 0)


if __name__ == "__main__":
    main()
