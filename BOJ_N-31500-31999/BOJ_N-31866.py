def main():
    J, I = map(int, input().split())

    if J in [0, 2, 5] and I not in [0, 2, 5]:
        print(">")
    elif [J, I] in [[0, 2], [2, 5], [5, 0]]:
        print(">")
    elif J not in [0, 2, 5] and I in [0, 2, 5]:
        print("<")
    elif [J, I] in [[2, 0], [5, 2], [0, 5]]:
        print("<")
    else:
        print("=")


if __name__ == "__main__":
    main()
