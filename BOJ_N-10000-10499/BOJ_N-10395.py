def main():
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    for i in range(5):
        if X[i] == Y[i]:
            print('N')
            break
    else:
        print('Y')


if __name__ == "__main__":
    main()
