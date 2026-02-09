def water_jug_dfs(jug1, jug2, target):
    visited = set()
    path = []

    def dfs(a, b):
        if (a, b) in visited:
            return False

        visited.add((a, b))
        path.append((a, b))

        if a == target or b == target:
            return True

        next_states = [
            (jug1, b),
            (a, jug2),
            (0, b),
            (a, 0),
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ]

        for na, nb in next_states:
            if dfs(na, nb):
                return True

        path.pop()
        return False

    if dfs(0, 0):
        return path
    return None


jug1 = int(input("Enter Jug 1 capacity: "))
jug2 = int(input("Enter Jug 2 capacity: "))
target = int(input("Enter Target amount: "))

solution = water_jug_dfs(jug1, jug2, target)

if solution:
    print("\nSolution steps:")
    for a, b in solution:
        print(f"({a}/{jug1}, {b}/{jug2})")
else:
    print("No solution exists")
