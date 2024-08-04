def main():
    x = [len(input().rstrip()) for _ in range(6)]
    print(f"Latitude {x[0]}:{x[1]}:{x[2]}")
    print(f"Longitude {x[3]}:{x[4]}:{x[5]}")


if __name__ == "__main__":
    main()
