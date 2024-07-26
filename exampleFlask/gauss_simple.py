import numpy as np

def gauss_simple(A, b):
    n = len(b)
    # Combine A and b into an augmented matrix
    Ab = np.column_stack((A, b))
    steps = [Ab.copy()]
    
    for i in range(n):
        # Partial pivoting
        max_element = abs(Ab[i:, i]).argmax() + i
        if i != max_element:
            Ab[i], Ab[max_element] = Ab[max_element], Ab[i].copy()
            steps.append(Ab.copy())
        
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
            steps.append(Ab.copy())
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]
    
    steps.append(x)
    return x, steps

def format_steps(steps):
    formatted_steps = []
    for i, step in enumerate(steps[:-1]):  # Exclude the last step which is the solution
        formatted_step = f"Step {i + 1}:\n" + np.array2string(step, precision=4, suppress_small=True)
        formatted_steps.append(formatted_step)
    
    # Format the solution
    solution = steps[-1]
    formatted_solution = "Solution:\n" + ", ".join([f"x{i+1} = {x:.4f}" for i, x in enumerate(solution)])
    formatted_steps.append(formatted_solution)
    
    return formatted_steps

