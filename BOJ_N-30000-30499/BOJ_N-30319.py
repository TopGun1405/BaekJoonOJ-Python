def main():
    YYYY, MM, DD = map(int, input().split('-'))
    print("GOOD" if MM < 9 else ("GOOD" if MM == 9 and DD <= 16 else "TOO LATE"))


if __name__ == "__main__":
    main()
