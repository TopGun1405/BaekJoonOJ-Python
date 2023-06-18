def main():
    text = input()

    happy, sad = text.count(":-)"), text.count(":-(")
    print("none" if happy == sad == 0
          else ("unsure" if happy == sad
                else ("happy" if happy > sad
                      else "sad")))


if __name__ == "__main__":
    main()
