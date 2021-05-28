class Literal:
    def __init__(self, value):
        self.value = value

    def is_true(self):
        return self.value > 0

    def is_satisfied_by(self, x):
        value = abs(self.value)

        if (x[value - 1] and not self.is_true()) or (not x[value - 1] and self.is_true()):
            return False

        return True


class Clause:
    def __init__(self, literals):
        self.literals = []

        for literal in literals:
            self.literals.append(Literal(literal))

    def is_satisfied_by(self, x):
        for literal in self.literals:
            if literal.is_satisfied_by(x):
                return True

        return False


def main():
    print("Algorithm I")


if __name__ == '__main__':
    main()
