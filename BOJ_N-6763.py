def main():
    limit = int(input())
    v = int(input())
    print("You are speeding and your fine is $500." if v >= limit + 31
          else "You are speeding and your fine is $270." if limit + 21 <= v <= limit + 30
          else "You are speeding and your fine is $100." if limit + 1 <= v <= limit + 20
          else "Congratulations, you are within the speed limit!")


if __name__ == "__main__":
    main()
