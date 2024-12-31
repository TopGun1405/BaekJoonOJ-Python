def main():
    rot = "left"
    while True:
        digits = list(map(int, input()))

        if digits == [9] * 5:
            break

        sum_digits = sum(digits[:2])
        if sum_digits == 0:
            pass
        elif sum_digits % 2 == 0:
            rot = "right" if rot == "left" else "right"
        elif sum(digits[:2]) % 2 == 1:
            rot = "left"

        print(f"{rot} {''.join(map(str, digits[2:]))}")


if __name__ == "__main__":
    main()
