def main():
    # C++ Prob
    class Rectangle:
        def __init__(self, width: int, height: int) -> None:
            self.width = width
            self.height = height

        def get_width(self) -> int:
            return self.width

        def get_height(self) -> int:
            return self.height

        def set_width(self, width: int) -> None:
            if width <= 0 or width > 1_000:
                return
            self.width = width

        def set_height(self, height: int) -> None:
            if height <= 0 or height > 2_000:
                return
            self.height = height

        def area(self) -> int:
            return self.width * self.height

        def perimeter(self) -> int:
            return 2 * (self.width + self.height)

        def is_square(self) -> bool:
            return self.width == self.height


if __name__ == "__main__":
    main()
