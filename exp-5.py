def is_safe(var, value, assignment, constraints):
    for (v1, v2) in constraints:
        if var == v1 and v2 in assignment and assignment[v2] == value:
            return False
        if var == v2 and v1 in assignment and assignment[v1] == value:
            return False
    return True


def backtracking(variables, domains, constraints, assignment):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for value in domains[var]:
        if is_safe(var, value, assignment, constraints):
            assignment[var] = value
            result = backtracking(variables, domains, constraints, assignment)
            if result:
                return result
            del assignment[var]

    return None


if __name__ == "__main__":

    variables = ('Ma', 'Ju', 'St', 'Am', 'Br',
                 'Jo', 'De', 'Al', 'Mi', 'Ke')

    domains = dict((v, ['red', 'green', 'blue', 'gray']) for v in variables)

    constraints = [
        ('Ma', 'Ju'),
        ('Ma', 'St'),
        ('Ju', 'St'),
        ('Ju', 'Am'),
        ('Ju', 'De'),
        ('Ju', 'Br'),
        ('St', 'Am'),
        ('St', 'Al'),
        ('St', 'Mi'),
        ('Am', 'Mi'),
        ('Am', 'Jo'),
        ('Am', 'De'),
        ('Br', 'De'),
        ('Br', 'Ke'),
        ('Jo', 'Mi'),
        ('Jo', 'Am'),
        ('Jo', 'De'),
        ('Jo', 'Ke'),
        ('De', 'Ke'),
    ]

    solution = backtracking(variables, domains, constraints, {})

    if solution:
        print("\nColor mapping:\n")
        for k, v in solution.items():
            print(k, "==>", v)
    else:
        print("No solution found")
