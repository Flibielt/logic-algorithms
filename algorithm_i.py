from random import randrange


class Literal:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Literal):
            if self.value == other.value:
                return True
        return False

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


def resolution(clause1, clause2):
    literals1 = clause1.literals
    literals2 = clause2.literals
    resolution_literals = []

    for l1 in literals1:
        for l2 in literals2:
            if l1.value + l2.value != 0:
                resolution_literals.append(l1)

    unique_literals = set(resolution_literals)

    return Clause(unique_literals)


def algorithm_i(clauses, n):
    print("Algorithm I")
    m = len(clauses)
    literals = []
    d = 0

    # todo: Generate x1, ..., xn values, there will be the values for the literals
    while True:
        # I2: Advance
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
            # I4: Negate l_d and search for falsified clauses (C_j)
            literals[d] = -1 * literals[d]
            j = find_falsified_clause(clauses, literals)

            if j < 0:
                break

            # I5: Resolution
            resolution_clause = resolution(clauses[i], clauses[j])
            if len(resolution_clause.literals) == 0:
                return False
            else:
                clauses.append(resolution_clause)
                m = len(clauses)
                i = m
                # todo: Update d with some value


def main():
    clauses = []
    algorithm_i(clauses, 5)


if __name__ == '__main__':
    main()
