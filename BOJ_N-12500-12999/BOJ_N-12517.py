def main():
    T = int(input())
    for x in range(1, T+1):
        C = input()

        print(f"Case #{x}: {C} is ruled by {'nobody' if C[-1] == 'y' else ('a queen' if C[-1] in ['a', 'e', 'i', 'o', 'u'] else 'a king')}.")


if __name__ == "__main__":
    main()
