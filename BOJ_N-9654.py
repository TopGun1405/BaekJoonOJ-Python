def main():
    ship_name = ["N2 Bomber", "J-Type 327", "NX Cruiser", "N1 Starfighter", "Royal Cruiser"]
    class_name = ["Heavy Fighter", "Light Combat", "Medium Fighter", "Medium Fighter", "Light Combat"]
    deployment = ["Limited", "Unlimited", "Limited", "Unlimited", "Limited"]
    in_service = [21, 1, 18, 25, 4]

    print("{:14} {:14} {:10} {:10}".format("SHIP NAME", "CLASS", "DEPLOYMENT", "IN SERVICE"))
    for i in range(5):
        print("{:14} {:14} {:10} {:<10}".format(ship_name[i], class_name[i], deployment[i], in_service[i]))


if __name__ == "__main__":
    main()
