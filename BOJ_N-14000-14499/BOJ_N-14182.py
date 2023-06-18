def main():
    while True:
        tax = int(input())
        if tax == 0:
            break
        print(int(tax * 0.8) if tax > 5_000_000
              else (int(tax * 0.9) if 1_000_000 < tax <= 5_000_000 else tax))


if __name__ == "__main__":
    main()
