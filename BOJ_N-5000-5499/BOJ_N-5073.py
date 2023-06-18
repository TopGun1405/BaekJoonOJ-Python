def main():
    while True:
        tri = list(map(int, input().split()))
        if tri[0] == 0:
            break
        t, a = sum(tri), max(tri)
        print("Invalid" if a >= t - a
              else ("Equilateral" if tri[0] == tri[1] == tri[2]
                    else ("Isosceles" if tri[0] == tri[1] or tri[1] == tri[2] or tri[2] == tri[0]
                          else "Scalene")))


if __name__ == "__main__":
    main()
