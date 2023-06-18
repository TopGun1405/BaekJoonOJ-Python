def main():
    M, D = map(int, input().split())
    d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cal = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}
    print(cal[(sum(d[:M - 1]) + D) % 7])


if __name__ == "__main__":
    main()
