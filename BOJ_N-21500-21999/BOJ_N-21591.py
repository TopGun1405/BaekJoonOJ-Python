def main():
    wc, hc, ws, hs = map(int, input().split())
    print(1 if wc - ws >= 2 and hc - hs >= 2 else 0)


if __name__ == "__main__":
    main()
