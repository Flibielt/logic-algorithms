import random


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
        if (x[0] and not self.is_true()) or (not x[0] and self.is_true()):
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


def create_clauses(clause_inputs):
    clauses = []

    for clause_input in clause_inputs:
        clauses.append(Clause(clause_input))

    return clauses


def is_strictly_distinct(literals, new_literal):
    for literal in literals:
        if literal == new_literal:
            return False
        elif abs(literal) == abs(new_literal):
            return False

    return True


def find_falsified_clause(clauses, literals):
    for i in range(0, len(clauses)):
        if not clauses[i].is_satisfied_by(literals):
            return i
    return -1


def resolution(clause1, clause2):
    literals1 = clause1.literals
    literals2 = clause2.literals
    resolution_literal_values = []

    for l1 in literals1:
        for l2 in literals2:
            if l1.value + l2.value != 0:
                resolution_literal_values.append(l1.value)

    unique_literal_values = set(resolution_literal_values)

    return Clause(unique_literal_values)


def algorithm_i(clauses, n, x):
    print("Algorithm I")
    len(clauses)
    literals = []
    d = 0

    while True:
        # I2: Advance
        if d == n:
            return literals
        else:
            l_d = random.choice(x)
            while not is_strictly_distinct(literals, l_d):
                l_d = random.choice(x)
            literals.append(l_d)
            d = d + 1

        # I3: Find falsified C_i
        i = find_falsified_clause(clauses, literals)
        while i > -1:
            # I4: Negate l_d and search for falsified clauses (C_j)
            literals[d - 1] = -1 * literals[d - 1]
            j = find_falsified_clause(clauses, literals)

            # No falsified clause was found, return to I2
            if j < 0:
                break

            # I5: Resolution
            resolution_clause = resolution(clauses[i], clauses[j])
            if len(resolution_clause.literals) == 0:
                return []
            else:
                clauses.append(resolution_clause)
                m = len(clauses) - 1
                i = m

                max_t = 0
                for t in range(0, len(literals)):
                    if -literals[t] in clauses[m].literals:
                        max_t = t
                d = max_t


def create_x(count):
    x = []

    for i in range(-count, 0):
        x.append(i)

    for i in range(1, count + 1):
        x.append(i)

    return x


def main():
    clause_inputs = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, -5],
        [1, 2, 3, -4, 5],
        [1, 2, -3, 4, 5],
        [1, -2, 3, 4, 5]
    ]
    clauses = create_clauses(clause_inputs)
    x = create_x(10)
    result = algorithm_i(clauses, 5, x)

    if len(result) > 0:
        print("Result: " + str(result))
    else:
        print("Unsatisfiable")


if __name__ == '__main__':
    main()
