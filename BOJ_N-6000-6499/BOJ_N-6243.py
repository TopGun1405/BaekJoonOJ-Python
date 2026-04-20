from math import floor


def main():
    mileage = 0
    total_mileage = []
    while True:
        data = input()

        if data == "#":
            print(*total_mileage, sep="\n")
            break

        if data == "0":
            total_mileage.append(mileage)
            mileage = 0
        else:
            OriginalCity, DistanceCity, ActualMiles, ClassCode = data.split()
            ActualMiles = int(ActualMiles)

            if ClassCode == "F":
                mileage += 2 * ActualMiles
            elif ClassCode == "B":
                mileage += floor(1.5 * ActualMiles + 0.5)
            else:
                mileage += max(500, ActualMiles)


if __name__ == "__main__":
    main()
