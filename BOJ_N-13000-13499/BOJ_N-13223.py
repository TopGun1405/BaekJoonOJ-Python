def main():
    curr_hh, curr_mm, curr_ss = map(int, input().split(':'))
    salt_hh, salt_mm, salt_ss = map(int, input().split(':'))

    Tc = curr_hh * 3600 + curr_mm * 60 + curr_ss
    Ts = salt_hh * 3600 + salt_mm * 60 + salt_ss

    if Tc >= Ts:
        Ts += 24 * 3600
    time = Ts - Tc

    hh, mm, ss = time // 3600, time % 3600 // 60, time % 60
    print("{:02d}:{:02d}:{:02d}".format(hh, mm, ss))


if __name__ == "__main__":
    main()
