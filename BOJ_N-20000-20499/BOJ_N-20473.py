def main():
    n = int(input())

    a2, a3 = 0, 0
    room = 100
    for i in range(n//3, -1, -1):
        for j in range(n//2, -1, -1):
            if 3*i + 2*j == n and room > i+j:
                a2, a3 = j, i
                room = min(room, i+j)

    print(a2, a3)


if __name__ == "__main__":
    main()
