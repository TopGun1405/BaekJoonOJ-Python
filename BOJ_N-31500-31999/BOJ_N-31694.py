def main():
    Algosia = list(map(int, input().split()))
    Bajtek = list(map(int, input().split()))

    tot_A, tot_B = 0, 0
    A, B = {n: 0 for n in range(11)}, {n: 0 for n in range(11)}
    for a, b in zip(Algosia, Bajtek):
        A[a] += 1
        B[b] += 1
        tot_A += a
        tot_B += b

    if tot_A > tot_B:
        print("Algosia")
    elif tot_A < tot_B:
        print("Bajtek")
    else:
        for i in range(10, -1, -1):
            if A[i] > B[i]:
                print("Algosia")
                break
            elif A[i] < B[i]:
                print("Bajtek")
                break
        else:
            print("remis")


if __name__ == "__main__":
    main()
