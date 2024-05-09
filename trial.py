import pyscipopt as scip


def simple_integer_program(n, C):

    # Create a new SCIP instance
    model = scip.Model()

    # Create binary decision variables x_i
    x = {}
    for i in range(1, n+1):
        x[i] = model.addVar(vtype="B", name=f"x_{i}")

    # Add constraint: sum(x_i) <= C
    model.addCons(scip.quicksum(x[i] for i in range(1, n+1)) <= C)

    # Set the objective: maximize sum(x_i)
    model.setObjective(scip.quicksum(x[i] for i in range(1, n+1)), "maximize")

    # Solve the problem
    model.optimize()

    # Get the solution
    if model.getStatus() == "optimal":
        solution = {i: model.getVal(x[i]) for i in range(1, n+1)}
        return solution
    else:
        print("No optimal solution found.")
        return None


# Example usage
n = 5  # Number of binary variables
C = 3  # Constraint threshold
solution = simple_integer_program(n, C)
if solution:
    print("Optimal solution found:")
    print(solution)
