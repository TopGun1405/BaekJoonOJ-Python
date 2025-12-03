def main():
    N = int(input())
    school = [input() for _ in range(N)]

    print(f"Yonsei {'Won!' if school.index('yonsei') < school.index('korea') else 'Lost...'}")


if __name__ == "__main__":
    main()
