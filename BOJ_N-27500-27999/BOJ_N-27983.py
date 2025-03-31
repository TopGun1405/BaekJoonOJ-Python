def main():
    N = int(input())
    X = list(map(int, input().split()))
    L = list(map(int, input().split()))
    C = input().split()

    for i in range(N-1):
        for j in range(i+1, N):
            if abs(X[i] - X[j]) > L[i] + L[j] or C[i] == C[j]:
                continue
            print("YES")
            print(i+1, j+1)
            break
        else:
            continue
        break
    else:
        print("NO")


if __name__ == "__main__":
    main()
    