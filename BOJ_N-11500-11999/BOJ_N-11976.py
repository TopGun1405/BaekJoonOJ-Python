def main():
    bronze_b, bronze_a = map(int, input().split())
    silver_b, silver_a = map(int, input().split())
    gold_b, gold_a = map(int, input().split())
    platinum_b, platinum_a = map(int, input().split())

    silver = silver_a - silver_b
    gold = gold_a - gold_b
    platinum = platinum_a - platinum_b

    print(platinum + gold + silver)
    print(platinum + gold)
    print(platinum)


if __name__ == "__main__":
    main()
