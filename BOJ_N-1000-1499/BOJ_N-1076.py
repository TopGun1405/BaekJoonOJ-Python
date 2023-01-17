def main():
    rst = {"black": 0, "brown": 1, "red": 2,
           "orange": 3, "yellow": 4, "green": 5,
           "blue": 6, "violet": 7, "grey": 8, "white": 9}
    color1, color2, color3 = input(), input(), input()
    print((rst[color1]*10 + rst[color2]) * (10 ** rst[color3]))


if __name__ == "__main__":
    main()
