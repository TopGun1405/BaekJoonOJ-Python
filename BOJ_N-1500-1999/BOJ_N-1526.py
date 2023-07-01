def main():
    N = int(input())
    while True:
        minsu = True
        for n in str(N):
            if n != '4' and n != '7':
                minsu = False
                N -= 1
        if minsu:
            print(N)
            break


if __name__ == "__main__":
    main()
