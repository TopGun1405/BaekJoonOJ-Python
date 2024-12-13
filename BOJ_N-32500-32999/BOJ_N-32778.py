def main():
    station_info = input()

    if "(" in station_info:
        open_character = station_info.index("(")
        station_name = station_info[:open_character-1]
        sub_station_name = station_info[open_character+1:-1]
    else:
        station_name = station_info
        sub_station_name = "-"

    print(station_name)
    print(sub_station_name)


if __name__ == "__main__":
    main()
