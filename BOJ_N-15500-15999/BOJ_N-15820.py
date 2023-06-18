def main():
    S1, S2 = map(int, input().split())
    sampleT = [list(map(int, input().split())) for _ in range(S1)]
    systemT = [list(map(int, input().split())) for _ in range(S2)]
    for t in sampleT:
        if t[0] != t[1]:
            print("Wrong Answer")
            break
    else:
        for t in systemT:
            if t[0] != t[1]:
                print("Why Wrong!!!")
                break
        else:
            print("Accepted")


if __name__ == "__main__":
    main()
