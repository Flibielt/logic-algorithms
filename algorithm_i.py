from random import randrange


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


def is_strictly_distinct(literals, new_literal):
    for literal in literals:
        if literal.value == new_literal:
            return False
        elif abs(literal.value) == abs(new_literal):
            return False

    return True


def find_falsified_clause(clauses, literals):
    for i in range(0, len(clauses)):
        for literal in literals:
            if not clauses[i].is_satisfied_by(literal):
                return i
    return -1


def algorithm_i(clauses, n):
    print("Algorithm I")
    m = len(clauses)
    literals = []
    d = 0

    while True:
        # I2: Advanced
        if d == n:
            return True
        else:
            l_d = randrange(-10, 11)
            while not is_strictly_distinct(literals, l_d):
                l_d = randrange(-10, 11)
            literals.append(l_d)
            d = d + 1

        # I3: Find falsified C_i
        i = find_falsified_clause(clauses, literals)
        while i > -1:
            # I4: Negate l_d and search for falsified clauses
            literals[d] = -1 * literals[d]
            j = find_falsified_clause(clauses, literals)

            if j < 0:
                break


def main():
    clauses = []
    algorithm_i(clauses, 5)


if __name__ == '__main__':
    main()
