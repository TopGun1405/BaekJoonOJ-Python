def main():
    for a in range(1, 10):
        print(f"? A {a}", flush=True)

        resp1 = int(input())

        if resp1 == 1:
            for b in range(1, 10):
                print(f"? B {b}", flush=True)

                resp2 = int(input())

                if resp2 == 1:
                    print(f"! {a + b}")
                    break
            else:
                continue

            break


if __name__ == "__main__":
    main()
