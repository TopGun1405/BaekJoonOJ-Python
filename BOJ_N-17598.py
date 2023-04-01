def main():
    votes = [input() for _ in range(9)]
    print(["Lion", "Tiger"][votes.count("Tiger") >= 5])


if __name__ == "__main__":
    main()
