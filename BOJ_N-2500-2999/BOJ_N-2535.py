def main():
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    students.sort(key=lambda k: k[2], reverse=True)

    countryCnt = {}
    for country, student, _ in students:
        if sum(countryCnt.values()) == 3:
            break

        if country not in countryCnt:
            countryCnt[country] = 1
            print(country, student)
        else:
            if countryCnt[country] < 2:
                countryCnt[country] += 1
                print(country, student)
            else:
                continue


if __name__ == "__main__":
    main()
