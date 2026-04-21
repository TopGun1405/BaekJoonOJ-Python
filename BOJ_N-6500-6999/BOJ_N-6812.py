def main():

    def convert_time(hour, minute, diff_h, diff_m=0):
        total_min = hour * 60 + minute
        total_min += diff_h * 60 + diff_m

        total_min %= (24 * 60)

        converted_hour = total_min // 60
        converted_min = total_min % 60

        return converted_hour * 100 + converted_min

    ottawa_time = int(input())

    h, m = ottawa_time // 100, ottawa_time % 100

    print(f"{ottawa_time} in Ottawa")
    print(f"{convert_time(h, m, -3)} in Victoria")
    print(f"{convert_time(h, m, -2)} in Edmonton")
    print(f"{convert_time(h, m, -1)} in Winnipeg")
    print(f"{convert_time(h, m, 0)} in Toronto")
    print(f"{convert_time(h, m, 1)} in Halifax")
    print(f"{convert_time(h, m, 1, 30)} in St. John's")


if __name__ == "__main__":
    main()
