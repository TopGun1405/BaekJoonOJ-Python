def main():
    while True:
        data = input().split()

        if data[0] == "0":
            break

        bedsNum, customers = int(data[0]), list(data[1])
        beds, failed = {}, {}
        for customer in customers:
            if customer not in beds:
                if len(beds) < bedsNum:
                    beds[customer] = 1
                else:
                    failed[customer] = 1
            elif customer in beds:
                del beds[customer]

        if len(failed) > 0:
            print(f"{len(failed)} customer(s) walked away.")
        else:
            print("All customers tanned successfully.")


if __name__ == "__main__":
    main()
