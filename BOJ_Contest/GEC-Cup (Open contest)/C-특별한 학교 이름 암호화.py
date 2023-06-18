def main():
    name = input()
    school = {"North London Collegiate School": "NLCS",
              "Branksome Hall Asia": "BHA",
              "Korea International School": "KIS",
              "St. Johnsbury Academy": "SJA"}
    for names in school:
        enc = ''.join(map(lambda s: s.lower(), names.replace('.', '').split()))[:10]
        for i in range(26):
            c = ''.join(map(lambda s: chr((ord(s) + i) if ord(s) + i <= 122 else 97 + (ord(s) + i - 123)), enc))
            if name == c:
                print(school[names])
                break
        else:
            continue


if __name__ == "__main__":
    main()
