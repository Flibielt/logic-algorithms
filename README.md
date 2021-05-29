# Logic algorithms project

University project for logic algorithms.

## Exercise 1

Construct the 16 B2→B function shortest form, only with if-then-else operations and the T, ⊥ constants.

T: Tautology (TRUE)

⊥: Unsatisfactory formula (FALSE)


## Exercise 2

Implement the algorithm I (Knuth 7.2.2.2. page 61)

![The description of the algorithm](img/algorithm_i.png)

## Literal
A literal is an atomic formula or its negation.

For a literal *l*, the complementary literal is a literal corresponding to the negation of *l*.

## Strictly distinct literals
Two literals are strictly distinct if they are distinct and moreover they are not complementary one to the other. We say that a set of literals is strictly distinct if it does not contain two complementary literals.

## Clause
In logic, a **clause** is an expression formed from a finite collection of literals (atoms or their negations). A clause is true either whenever at least one of the literals that form it is true (a disjunctive clause, the most common use of the term), or when all the literals that form it are true (a conjunctive clause, a less common use of the term).