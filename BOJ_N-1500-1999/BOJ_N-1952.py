def main():
    M, N = map(int, input().split())

    print(N*2-1 if M > N else M*2-2)


if __name__ == "__main__":
    main()
