def main():
    x_A, y_A, x_B, y_B, x_C, y_C = map(int, input().split())
    
    # (y_A - y_B) / (x_A - x_B) == (y_C - y_A) / (x_C - x_A)
    if (x_A - x_B) * (y_C - y_A) == (y_A - y_B) * (x_C - x_A):
        print(-1)
    else:
        AB = ((x_A - x_B) ** 2 + (y_A - y_B) ** 2) ** 0.5
        CA = ((x_C - x_A) ** 2 + (y_C - y_A) ** 2) ** 0.5
        BC = ((x_B - x_C) ** 2 + (y_B - y_C) ** 2) ** 0.5

        length = [AB + BC, AB + CA, BC + CA]
        print(2 * (max(length) - min(length)))


if __name__ == "__main__":
    main()
