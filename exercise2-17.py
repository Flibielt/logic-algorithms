class Domino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = 'x'

    def __eq__(self, other):
        if isinstance(other, Domino):
            if self.x == other.x and self.y == other.y:
                return True
        return False


class DominoCircle:
    def __init__(self):
        self.array = []

    def __eq__(self, other):
        if isinstance(other, DominoCircle):
            if len(self.array) != len(other.array):
                return False

            first_domino = self.array[0]

            # Search the first domino
            first_domino_index = -1
            for i in range(0, len(self.array)):
                if first_domino.__eq__(other.array[i]):
                    first_domino_index = i
                    break

            # The other circle does not contain the domino
            if first_domino_index == -1:
                return False

            # Compare the two circle with the same direction
            index = 0
            equal = True
            for other_index in range(first_domino_index, first_domino_index + len(self.array)):
                if not self.array[index].__eq__(other.array[other_index % len(self.array)]):
                    equal = False
                    break
                index = index + 1

            # If not equals, then compare the two circles in the opposite direction
            if not equal:
                index = 0
                equal = True
                for other_index in range(first_domino_index, first_domino_index - len(self.array), -1):
                    if not self.array[index].__eq__(other.array[other_index % len(self.array)]):
                        equal = False
                        break
                    index = index + 1

            return equal


def generate_domino():
    domino_array = []
    for i in range(0, 7):
        for j in range(i, 7):
            domino_array.append(Domino(i, j))

    return domino_array


def main():
    print("Search domino circles")
    count = 0


if __name__ == "__main__":
    main()
