from scipy.optimize import linprog

def main():
    try:
        # Get the number of variables
        num_vars = int(input("Enter the number of variables: "))
        if num_vars <= 0:
            raise ValueError("Number of variables must be positive.")

        # Get coefficients of the objective function
        print("Enter the coefficients of the objective function (space-separated):")
        c = list(map(float, input().split()))
        if len(c) != num_vars:
            raise ValueError(f"Expected {num_vars} coefficients.")

        c = [-coef for coef in c]  # Negate for minimization

        # Get the number of constraints
        num_constraints = int(input("Enter the number of constraints: "))
        if num_constraints <= 0:
            raise ValueError("Number of constraints must be positive.")
        
        A = []
        b = []
        
        for i in range(num_constraints):
            print(f"Enter the coefficients for constraint {i + 1} (space-separated):")
            constraint = list(map(float, input().split()))
            if len(constraint) != num_vars:
                raise ValueError(f"Expected {num_vars} coefficients for constraint {i + 1}.")
            A.append(constraint)

            print(f"Enter the right-hand side value for constraint {i + 1}:")
            rhs = float(input())
            b.append(rhs)

        # Get variable bounds
        bounds = []
        for i in range(num_vars):
            print(f"Enter the bounds for variable x{i + 1} (min max, space-separated, or just hit enter for [0, None]):")
            bounds_input = input()
            if bounds_input:
                min_val, max_val = map(float, bounds_input.split())
                if min_val > max_val:
                    raise ValueError("Minimum bound cannot be greater than maximum bound.")
                bounds.append((min_val, max_val))
            else:
                bounds.append((0, None))  # Default non-negativity

        # Run the Simplex method
        result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

        # Display the results
        if result.success:
            print(f"Optimal value: {-result.fun}")  # Negate again to get the max value
            for i in range(num_vars):
                print(f"x{i + 1}: {result.x[i]}")
        else:
            print("No solution found.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()