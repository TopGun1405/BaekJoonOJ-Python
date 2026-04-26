def main():
    N = int(input())

    for i in range(1, N+1):
        print(" "*(2*N-i) + "*" + " "*N + "*" + " "*(2*i-1) + "*" + " "*(N-i))
    for i in range(N+1, 2*N+1):
        print(" "*(2*N-i) + "*" + " "*(2*i-N-1) + "*" + " "*(2*N-2*(i-N)+1) + "*" + " "*(i-N-1))


if __name__ == "__main__":
    main()
