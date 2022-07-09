import time

from graph import graph
from csp_solution import MinConflictSolution, backtracking_solution
def build_matrix(rows, cols):
    matrix = []
    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])
    cnt = 1
    for i in range(N):
        for j in range(N):
            matrix[i][j] = cnt
            cnt += 1
    return matrix
def inARowOrCol(x,y,matrix):
    i1,i2 =0,0
    j1,j2 =0,0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == x:
                i1 , j1 = i, j
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == y:
                i2 , j2 = i, j
    return (i1==i2 or j1==j2)
def generate_graph(matrix):
    b = []
    for i in range(N*N):
        for j in range(N*N):
            if i+1 != j+1:
                if inARowOrCol(i + 1, j + 1, matrix):
                    b.append((str(i+1), str(j+1)))
    return b

N = int(input("Enter N :"))
regions = []
matrix = build_matrix(N,N)
# print(build_matrix(N,N))
cnt = 1
for i in range(N):
    for j in range(N):
        regions.append(str(cnt))
        cnt += 1
# print(regions)

borders = generate_graph(matrix)
# print(borders)

print("Constraint list (borders list) : ",borders)
colors = []
cnt = 1
for i in range(N):
    colors.append(str(cnt))
    cnt += 1

def check_border(variables, *args):
    zipped = list(zip(variables, args))
    return zipped[0][1] != zipped[1][1]

def solve_csp(solver):
    problem = graph(solver)
    problem.add_variables(regions, colors)
    for node in regions:
        borders_per_node = [borders[index] for (index, a_tuple) in enumerate(borders) if a_tuple[0] == node]
        if borders_per_node:
            for border in borders_per_node:
                problem.add_constraint(check_border, list(border))

    start_time = time.time()
    problem.get_solution()
    end_time = (time.time() - start_time)
    print(f"Solution with {solver.get_description()} took {end_time} sec and {solver.counter} checks")
    problem.printsolutions(N)

if __name__ == "__main__":
    solvers = [backtracking_solution(forwardcheck=False), backtracking_solution(forwardcheck=True), MinConflictSolution()]
    for solver in solvers:
        solve_csp(solver)