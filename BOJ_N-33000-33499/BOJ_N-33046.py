def main():
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    vib = 0
    for _ in range(A+B+C+D-1):
        if vib == 4:
            vib = 1
            continue
        vib += 1

    print(vib)


if __name__ == "__main__":
    main()
