def multiply_single_iteration(n, m):
    return n * m

def multiply_n_iterations(n, m):
    result = 0
    for _ in range(m):
        result += n
    return result
n = 5
m = 3
print(multiply_single_iteration(n, m)) 
print(multiply_n_iterations(n, m))   