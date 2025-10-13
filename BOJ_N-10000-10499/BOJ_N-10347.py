def main():
    shift = {chr(i): chr(i+1) for i in range(65, 90)}
    shift.update({'Z': "_", '_': ".", '.': "A"})
    while True:
        C = input().split()

        if C[0] == "0":
            break

        N, S = int(C[0]), list(C[1])
        S = S[::-1]
        for _ in range(N):
            for i in range(len(S)):
                S[i] = shift[S[i]]

        print("".join(S))


if __name__ == "__main__":
    main()
